#!/usr/bin/env python3
"""Check the generated logos against a real SVG renderer.

``build_logos.py`` computes bounding boxes analytically (``svgpath.py``) so it
stays pure-stdlib. This script rasterizes each generated file with
``rsvg-convert`` and measures where the ink actually lands, confirming that:

  1. every mark is centered in the 24-unit band, and
  2. every mark hits its optical target size.

Requires librsvg (``brew install librsvg``). It is a development check only --
not needed to build the logos, and not needed to render the README.

Usage:
    python3 scripts/verify_logos.py
"""

from __future__ import annotations

import pathlib
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_logos import CANVAS_H, LOGOS, MARK_BAND, OUT_DIR, TARGET_GEOMEAN  # noqa: E402

SCALE = 20  # px per SVG user unit
TOL = 0.35  # user units; ~1.5% of the mark band


def decode_rgba(png: bytes) -> tuple[int, int, bytes]:
    """Decode a non-interlaced 8-bit RGBA PNG to raw pixels."""
    if png[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")

    pos, idat, w, h = 8, [], 0, 0
    while pos < len(png):
        (length,) = struct.unpack(">I", png[pos:pos + 4])
        ctype = png[pos + 4:pos + 8]
        data = png[pos + 8:pos + 8 + length]
        if ctype == b"IHDR":
            w, h, depth, color, _, _, interlace = struct.unpack(">IIBBBBB", data)
            if (depth, color, interlace) != (8, 6, 0):
                raise ValueError(
                    f"want 8-bit RGBA non-interlaced, got {depth}/{color}/{interlace}"
                )
        elif ctype == b"IDAT":
            idat.append(data)
        elif ctype == b"IEND":
            break
        pos += 12 + length

    raw = zlib.decompress(b"".join(idat))
    stride, bpp = w * 4, 4
    out = bytearray(w * h * 4)
    prev = bytearray(stride)
    p = 0
    for y in range(h):
        ft = raw[p]
        p += 1
        line = bytearray(raw[p:p + stride])
        p += stride
        for i in range(stride):
            a = line[i - bpp] if i >= bpp else 0
            b = prev[i]
            c = prev[i - bpp] if i >= bpp else 0
            if ft == 1:
                line[i] = (line[i] + a) & 0xFF
            elif ft == 2:
                line[i] = (line[i] + b) & 0xFF
            elif ft == 3:
                line[i] = (line[i] + (a + b) // 2) & 0xFF
            elif ft == 4:
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pred = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pred) & 0xFF
            elif ft != 0:
                raise ValueError(f"bad filter {ft}")
        out[y * stride:(y + 1) * stride] = line
        prev = line
    return w, h, bytes(out)


def ink_bbox(w: int, h: int, px: bytes, thresh: int = 8):
    """Tight bbox of non-transparent pixels, in pixel coords."""
    x0, y0, x1, y1 = w, h, -1, -1
    for y in range(h):
        row = y * w * 4
        for x in range(w):
            if px[row + x * 4 + 3] >= thresh:
                if x < x0: x0 = x
                if x > x1: x1 = x
                if y < y0: y0 = y
                if y > y1: y1 = y
    if x1 < 0:
        raise ValueError("no ink")
    return x0, y0, x1 + 1, y1 + 1


def main() -> int:
    if not shutil.which("rsvg-convert"):
        print("rsvg-convert not found (brew install librsvg) -- skipping", file=sys.stderr)
        return 0

    failures = 0
    print(f"{'logo':10s} {'ink w x h':>16s} {'geomean':>9s} {'gap top/bot':>16s}  status")
    print("-" * 68)

    with tempfile.TemporaryDirectory() as td:
        for logo in LOGOS:
            src = OUT_DIR / f"{logo.slug}.svg"
            out = pathlib.Path(td) / f"{logo.slug}.png"
            subprocess.run(
                ["rsvg-convert", "-h", str(CANVAS_H * SCALE), str(src), "-o", str(out)],
                check=True, capture_output=True,
            )
            w, h, px = decode_rgba(out.read_bytes())
            x0, y0, x1, y1 = ink_bbox(w, h, px)

            mw, mh = (x1 - x0) / SCALE, (y1 - y0) / SCALE
            geomean = (mw * mh) ** 0.5
            top = y0 / SCALE
            bottom = MARK_BAND - y1 / SCALE

            problems = []
            # the mark must be vertically centered within the band
            if abs(top - bottom) > TOL:
                problems.append(f"off-center by {abs(top - bottom):.2f}")
            # and must hit the optical target, unless a clamp bound it
            clamped = mh >= MARK_BAND - TOL
            if not clamped and abs(geomean - TARGET_GEOMEAN) > TOL:
                problems.append(f"geomean {geomean:.2f} != {TARGET_GEOMEAN}")

            status = "ok" if not problems else "FAIL: " + ", ".join(problems)
            failures += bool(problems)
            print(f"{logo.slug:10s} {mw:7.2f} x {mh:6.2f} {geomean:9.2f} "
                  f"{top:7.2f} /{bottom:7.2f}  {status}")

    print()
    if failures:
        print(f"{failures} logo(s) failed", file=sys.stderr)
        return 1
    print("all logos verified against rsvg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
