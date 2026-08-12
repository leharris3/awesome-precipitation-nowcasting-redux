"""Minimal SVG path geometry: tight bounding boxes, pure stdlib.

Used by ``build_logos.py`` to optically normalize marks. Only the bounding box
is needed, so curves are densely sampled rather than solved analytically --
at SAMPLES=64 the error is far below the precision we round to.

Cross-checked against a real renderer by ``scripts/verify_logos.py``.
"""

from __future__ import annotations

import math
import re

SAMPLES = 64

_NUM = r"[+-]?(?:\d*\.\d+|\d+\.?)(?:[eE][+-]?\d+)?"
_NUM_RE = re.compile(_NUM)
_CMD_RE = re.compile(r"[MmZzLlHhVvCcSsQqTtAa]")

# Arc flags are single characters and may be packed against the next number
# ("a1.6 1.6 0 11-3.2 0" means flags 1,1 then x=-3.2). A generic number scanner
# reads that "11" as eleven, so arcs need their own grammar.
_SEP = r"[\s,]*"
_ARC_RE = re.compile(
    f"({_NUM}){_SEP}({_NUM}){_SEP}({_NUM}){_SEP}([01]){_SEP}([01]){_SEP}({_NUM}){_SEP}({_NUM})"
)

# how many numbers each command consumes per repetition
_ARITY = {
    "M": 2, "L": 2, "H": 1, "V": 1,
    "C": 6, "S": 4, "Q": 4, "T": 2,
    "A": 7, "Z": 0,
}


def _tokenize(d: str) -> list[tuple[str, list[float]]]:
    """Split path data into (command, args) groups, expanding implicit repeats."""
    out: list[tuple[str, list[float]]] = []
    for m in _CMD_RE.finditer(d):
        cmd = m.group()
        # this command's numbers run from just after its letter to the next letter
        chunk = d[m.end():]
        nxt = _CMD_RE.search(chunk)
        chunk = chunk[: nxt.start()] if nxt else chunk

        arity = _ARITY[cmd.upper()]
        if arity == 0:
            out.append((cmd, []))
            continue

        if cmd.upper() == "A":
            groups = [[float(g) for g in mm.groups()] for mm in _ARC_RE.finditer(chunk)]
            if not groups:
                raise ValueError(f"command {cmd!r} has no parsable arc arguments")
            nums = [v for g in groups for v in g]
        else:
            nums = [float(x.group()) for x in _NUM_RE.finditer(chunk)]
            if not nums or len(nums) % arity:
                raise ValueError(
                    f"command {cmd!r} got {len(nums)} args, need a multiple of {arity}"
                )

        for i in range(0, len(nums), arity):
            group = nums[i: i + arity]
            # a repeated M/m continues as an implicit L/l per the SVG spec
            if i and cmd == "M":
                out.append(("L", group))
            elif i and cmd == "m":
                out.append(("l", group))
            else:
                out.append((cmd, group))
    return out


def _cubic(p0, p1, p2, p3, t):
    u = 1 - t
    return (
        u * u * u * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t * t * t * p3[0],
        u * u * u * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t * t * t * p3[1],
    )


def _quad(p0, p1, p2, t):
    u = 1 - t
    return (
        u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
        u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1],
    )


def _arc_points(p0, rx, ry, phi_deg, large_arc, sweep, p1):
    """Endpoint -> center parameterization (SVG implementation notes F.6.5)."""
    x0, y0 = p0
    x1, y1 = p1
    if rx == 0 or ry == 0 or (x0 == x1 and y0 == y1):
        return [p1]

    rx, ry = abs(rx), abs(ry)
    phi = math.radians(phi_deg)
    cos_p, sin_p = math.cos(phi), math.sin(phi)

    dx2, dy2 = (x0 - x1) / 2.0, (y0 - y1) / 2.0
    x1p = cos_p * dx2 + sin_p * dy2
    y1p = -sin_p * dx2 + cos_p * dy2

    # scale up radii if they cannot span the endpoints (F.6.6)
    lam = (x1p * x1p) / (rx * rx) + (y1p * y1p) / (ry * ry)
    if lam > 1:
        s = math.sqrt(lam)
        rx, ry = rx * s, ry * s

    num = rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p
    den = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    coef = math.sqrt(max(num / den, 0.0))
    if large_arc == sweep:
        coef = -coef
    cxp = coef * rx * y1p / ry
    cyp = -coef * ry * x1p / rx

    cx = cos_p * cxp - sin_p * cyp + (x0 + x1) / 2.0
    cy = sin_p * cxp + cos_p * cyp + (y0 + y1) / 2.0

    def angle(ux, uy, vx, vy):
        dot = ux * vx + uy * vy
        n = math.hypot(ux, uy) * math.hypot(vx, vy)
        a = math.acos(max(-1.0, min(1.0, dot / n)))
        return -a if (ux * vy - uy * vx) < 0 else a

    theta0 = angle(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dtheta = angle((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not sweep and dtheta > 0:
        dtheta -= 2 * math.pi
    elif sweep and dtheta < 0:
        dtheta += 2 * math.pi

    pts = []
    for i in range(1, SAMPLES + 1):
        th = theta0 + dtheta * i / SAMPLES
        pts.append((
            cos_p * rx * math.cos(th) - sin_p * ry * math.sin(th) + cx,
            sin_p * rx * math.cos(th) + cos_p * ry * math.sin(th) + cy,
        ))
    return pts


def bbox(d: str) -> tuple[float, float, float, float]:
    """Return the tight (x0, y0, x1, y1) bounding box of path data `d`."""
    xs: list[float] = []
    ys: list[float] = []

    cur = (0.0, 0.0)
    start = (0.0, 0.0)
    prev_cubic_ctl: tuple[float, float] | None = None
    prev_quad_ctl: tuple[float, float] | None = None

    def add(pts):
        for x, y in pts:
            xs.append(x)
            ys.append(y)

    for cmd, a in _tokenize(d):
        rel = cmd.islower()
        c = cmd.upper()
        cx, cy = cur

        if c == "M":
            cur = (a[0] + cx, a[1] + cy) if rel else (a[0], a[1])
            start = cur
            add([cur])
            prev_cubic_ctl = prev_quad_ctl = None
            continue
        if c == "Z":
            cur = start
            add([cur])
            prev_cubic_ctl = prev_quad_ctl = None
            continue

        if c == "L":
            cur = (a[0] + cx, a[1] + cy) if rel else (a[0], a[1])
            add([cur])
            prev_cubic_ctl = prev_quad_ctl = None
        elif c == "H":
            cur = (a[0] + cx, cy) if rel else (a[0], cy)
            add([cur])
            prev_cubic_ctl = prev_quad_ctl = None
        elif c == "V":
            cur = (cx, a[0] + cy) if rel else (cx, a[0])
            add([cur])
            prev_cubic_ctl = prev_quad_ctl = None
        elif c in ("C", "S"):
            if c == "C":
                p1 = (a[0] + cx, a[1] + cy) if rel else (a[0], a[1])
                p2 = (a[2] + cx, a[3] + cy) if rel else (a[2], a[3])
                p3 = (a[4] + cx, a[5] + cy) if rel else (a[4], a[5])
            else:
                # reflect the previous control point about the current point
                p1 = ((2 * cx - prev_cubic_ctl[0], 2 * cy - prev_cubic_ctl[1])
                      if prev_cubic_ctl else (cx, cy))
                p2 = (a[0] + cx, a[1] + cy) if rel else (a[0], a[1])
                p3 = (a[2] + cx, a[3] + cy) if rel else (a[2], a[3])
            add([_cubic(cur, p1, p2, p3, i / SAMPLES) for i in range(SAMPLES + 1)])
            prev_cubic_ctl, prev_quad_ctl = p2, None
            cur = p3
        elif c in ("Q", "T"):
            if c == "Q":
                p1 = (a[0] + cx, a[1] + cy) if rel else (a[0], a[1])
                p2 = (a[2] + cx, a[3] + cy) if rel else (a[2], a[3])
            else:
                p1 = ((2 * cx - prev_quad_ctl[0], 2 * cy - prev_quad_ctl[1])
                      if prev_quad_ctl else (cx, cy))
                p2 = (a[0] + cx, a[1] + cy) if rel else (a[0], a[1])
            add([_quad(cur, p1, p2, i / SAMPLES) for i in range(SAMPLES + 1)])
            prev_quad_ctl, prev_cubic_ctl = p1, None
            cur = p2
        elif c == "A":
            end = (a[5] + cx, a[6] + cy) if rel else (a[5], a[6])
            add(_arc_points(cur, a[0], a[1], a[2], bool(a[3]), bool(a[4]), end))
            cur = end
            prev_cubic_ctl = prev_quad_ctl = None

    if not xs:
        raise ValueError("path produced no points")
    return min(xs), min(ys), max(xs), max(ys)
