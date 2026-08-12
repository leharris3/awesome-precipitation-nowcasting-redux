#!/usr/bin/env python3
"""Generate the normalized org logos used by the README section headings.

Why this exists
---------------
The README used to embed logos by hotlinking Google's favicon service
(``https://www.google.com/s2/favicons?domain=...``). That was fragile:

* the endpoint 301-redirects, and GitHub's image proxy (camo) caches the
  result opaquely, so logos could silently stop resolving;
* it returns whatever raster the site happens to ship -- in practice a mix of
  32x32, 48x48 and 64x64 PNGs -- so scaling them all to one CSS height gave
  each logo a different optical weight and blur;
* favicons carry arbitrary internal padding, so no two marks shared a
  baseline, which is what made the headings look misaligned.

The fix is to stop hotlinking and instead vendor every mark locally on a
single shared canvas. Source paths come from simple-icons, which authors every
icon on an identical 24x24 grid -- that shared grid is what makes the marks
line up with each other. Each mark is then re-emitted on a 24x27 canvas: the
extra 3 units of empty space below the mark offset ``vertical-align: middle``
(which centers on the x-height, sitting slightly low next to heading text) so
the logo ends up optically centered on the heading's cap height.

Colors are deliberately monochrome and chosen to stay legible on both GitHub's
light (#ffffff) and dark (#0d1117) canvases, which avoids needing a
``<picture>`` + ``prefers-color-scheme`` pair per logo.

Usage
-----
    python3 scripts/build_logos.py

Re-run after editing ``LOGOS`` to add an org. Output is committed to the repo,
so the README has no network dependency at render time.
"""

from __future__ import annotations

import math
import re
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import svgpath  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "assets" / "logos"

# simple-icons v11 is pinned deliberately: later majors dropped several of the
# corporate marks used here (microsoft and ibm are 404 on v13+). Pinning keeps
# this script reproducible; the generated SVGs are committed either way.
SIMPLE_ICONS_CDN = "https://cdn.jsdelivr.net/npm/simple-icons@11/icons/{slug}.svg"

# Shared canvas. The mark is centered in a MARK_BAND-tall band; MARK_PAD_BOTTOM
# units of empty space below it do the baseline compensation described above.
# Canvas *height* is what's shared -- width is per-logo (see TARGET_GEOMEAN).
MARK_BAND = 24
MARK_PAD_BOTTOM = 3
CANVAS_H = MARK_BAND + MARK_PAD_BOTTOM

# Optical sizing. Fitting every mark into a common box is wrong: simple-icons
# fits marks by bounding box, so a square mark (Google's G) fills 24x24 while a
# wide wordmark (IBM, NASA) hits the width limit and ends up only ~9 units tall
# -- it reads as far smaller even though both technically "fill" the box.
#
# Normalizing on the geometric mean of the bounding box instead equalizes
# optical area, so square marks and wide wordmarks carry the same visual weight.
# Marks stay within MARK_BAND tall and MAX_MARK_W wide.
TARGET_GEOMEAN = 19.0
MAX_MARK_W = 40.0


@dataclass(frozen=True)
class Logo:
    """One org mark.

    ``slug`` names the output file. ``source`` is a simple-icons slug, or None
    when ``path`` is supplied inline (for orgs simple-icons does not carry).
    ``color`` must read acceptably on both a white and a #0d1117 background.
    ``stroke_width`` switches the path from filled to stroked, which inline
    glyphs need; simple-icons paths are always filled.
    """

    slug: str
    label: str
    color: str
    source: str | None = None
    path: str | None = None
    stroke_width: float | None = None


# A generic radar-sweep glyph for NOAA: three concentric arcs over a dot,
# centered on (12, 18) with a 30-degree half-angle, sized so the outer arc plus
# its stroke exactly spans the 24-unit width.
#
# NOAA's actual seal is US government insignia whose use is restricted (it may
# not be used in any way implying endorsement), so we deliberately do not
# reproduce it. This is a neutral domain icon standing in for the org.
NOAA_RADAR_PATH = (
    "M1.26 11.8A12.4 12.4 0 0 1 22.74 11.8"
    "M4.9 13.9A8.2 8.2 0 0 1 19.1 13.9"
    "M8.54 16A4 4 0 0 1 15.46 16"
    "M12 18h0"
)

LOGOS: tuple[Logo, ...] = (
    Logo("google", "Google", "#4285F4", source="google"),
    Logo("nvidia", "NVIDIA", "#76B900", source="nvidia"),
    Logo("microsoft", "Microsoft", "#0078D4", source="microsoft"),
    Logo("amazon", "Amazon", "#FF9900", source="amazon"),
    Logo("ibm", "IBM", "#4589FF", source="ibm"),
    Logo("nasa", "NASA", "#E03C31", source="nasa"),
    Logo("noaa", "NOAA", "#0085CA", path=NOAA_RADAR_PATH, stroke_width=2.4),
)

_PATH_RE = re.compile(r'<path[^>]*\sd="([^"]+)"')
_VIEWBOX_RE = re.compile(r'viewBox="([^"]+)"')


def fetch_simple_icon(slug: str) -> str:
    """Return the single path data string for a simple-icons mark."""
    url = SIMPLE_ICONS_CDN.format(slug=slug)
    with urllib.request.urlopen(url, timeout=30) as resp:
        if resp.status != 200:
            raise RuntimeError(f"{slug}: HTTP {resp.status} from {url}")
        svg = resp.read().decode("utf-8")

    viewbox = _VIEWBOX_RE.search(svg)
    if not viewbox or viewbox.group(1).split() != ["0", "0", "24", "24"]:
        # The whole alignment guarantee rests on every mark sharing one grid.
        raise RuntimeError(
            f"{slug}: expected a 0 0 24 24 viewBox, got {viewbox and viewbox.group(1)!r}"
        )

    paths = _PATH_RE.findall(svg)
    if len(paths) != 1:
        raise RuntimeError(f"{slug}: expected exactly 1 <path>, found {len(paths)}")
    return paths[0]


def _fmt(v: float) -> str:
    """Trim float noise out of the emitted markup."""
    return f"{v:.4f}".rstrip("0").rstrip(".") or "0"


def render(logo: Logo, path_data: str) -> tuple[str, float]:
    """Emit the normalized SVG for one logo, plus its canvas width."""
    x0, y0, x1, y1 = svgpath.bbox(path_data)

    # a stroked path inks half its width beyond the geometry on every side
    if logo.stroke_width is not None:
        half = logo.stroke_width / 2.0
        x0, y0, x1, y1 = x0 - half, y0 - half, x1 + half, y1 + half

    w, h = x1 - x0, y1 - y0
    if w <= 0 or h <= 0:
        raise RuntimeError(f"{logo.slug}: degenerate bounding box {w}x{h}")

    scale = TARGET_GEOMEAN / math.sqrt(w * h)
    scale = min(scale, MARK_BAND / h, MAX_MARK_W / w)  # clamp to the canvas
    sw, sh = w * scale, h * scale

    # center the mark: horizontally in the canvas, vertically in the mark band
    canvas_w = sw
    tx = (canvas_w - sw) / 2.0 - x0 * scale
    ty = (MARK_BAND - sh) / 2.0 - y0 * scale

    if logo.stroke_width is not None:
        paint = (
            f'fill="none" stroke="{logo.color}" '
            f'stroke-width="{_fmt(logo.stroke_width)}" stroke-linecap="round"'
        )
    else:
        paint = f'fill="{logo.color}"'

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {_fmt(canvas_w)} {CANVAS_H}" '
        f'width="{_fmt(canvas_w)}" height="{CANVAS_H}" '
        f'role="img" aria-label="{logo.label}">'
        f"<title>{logo.label}</title>"
        f'<g transform="translate({_fmt(tx)} {_fmt(ty)}) scale({_fmt(scale)})">'
        f'<path {paint} d="{path_data}"/>'
        f"</g></svg>\n"
    )
    return svg, canvas_w


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for logo in LOGOS:
        if logo.path is not None:
            path_data = logo.path
            origin = "inline"
        elif logo.source is not None:
            path_data = fetch_simple_icon(logo.source)
            origin = f"simple-icons/{logo.source}"
        else:
            raise RuntimeError(f"{logo.slug}: needs either `source` or `path`")

        svg, canvas_w = render(logo, path_data)
        dest = OUT_DIR / f"{logo.slug}.svg"
        dest.write_text(svg, encoding="utf-8")
        print(
            f"wrote {str(dest.relative_to(REPO_ROOT)):28s} "
            f"{canvas_w:5.1f}x{CANVAS_H}  {logo.color}  ({origin})"
        )

    print(f"\n{len(LOGOS)} logos, shared canvas height {CANVAS_H}, "
          f"optical size {TARGET_GEOMEAN}.")
    print('Embed with: <img src="assets/logos/<slug>.svg" height="24" align="middle" alt="">')
    return 0


if __name__ == "__main__":
    sys.exit(main())
