"""Generate 3 candidate marketplace icons (128x128 PNG) for ULTR[A] MFD.

Each candidate explores a different design direction. Pick a winner and we
replace icons/icon.png with the chosen file.
"""
from PIL import Image, ImageDraw, ImageFilter
import os

SIZE = 128
IRON = (15, 14, 12)
AMBER = (255, 184, 30)
AMBER_BODY = (255, 174, 59)
AMBER_DEEP = (160, 107, 10)

OUT = "icons/candidates"
os.makedirs(OUT, exist_ok=True)


def add_glow(img, glow_color=AMBER_BODY, blur=4, opacity=0.55):
    """Returns img with a soft glow halo behind any amber pixels."""
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    pixels = img.load()
    glow_px = glow.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y][:3]
            if r > 100 and g > 50 and b < 100:
                glow_px[x, y] = (*glow_color, int(255 * opacity))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=blur))
    composite = Image.new("RGB", img.size, IRON)
    composite.paste(glow, (0, 0), glow)
    composite.paste(img, (0, 0))
    return composite


def save_png(img, name):
    path = os.path.join(OUT, name)
    img.save(path, "PNG")
    print(f"  wrote {path}  ({os.path.getsize(path)} bytes)")


# ============================================================
# A1 — Bracketed stencil [A]
# ============================================================
def candidate_a1():
    img = Image.new("RGB", (SIZE, SIZE), IRON)
    draw = ImageDraw.Draw(img)

    # Left bracket
    draw.rectangle([18, 24, 26, 104], fill=AMBER)
    draw.rectangle([18, 24, 40, 32], fill=AMBER)
    draw.rectangle([18, 96, 40, 104], fill=AMBER)

    # Right bracket (mirror)
    draw.rectangle([102, 24, 110, 104], fill=AMBER)
    draw.rectangle([88, 24, 110, 32], fill=AMBER)
    draw.rectangle([88, 96, 110, 104], fill=AMBER)

    # Center stencil A — diagonal legs as ellipses with a stencil gap
    A_top = (64, 38)
    A_bl = (46, 100)
    A_br = (82, 100)
    A_stroke = 7
    for i in range(0, 65):
        t = i / 64
        x_l = int(A_top[0] + (A_bl[0] - A_top[0]) * t)
        y_l = int(A_top[1] + (A_bl[1] - A_top[1]) * t)
        x_r = int(A_top[0] + (A_br[0] - A_top[0]) * t)
        y_r = int(A_top[1] + (A_br[1] - A_top[1]) * t)
        if not (0.38 <= t <= 0.44):
            draw.ellipse([x_l - A_stroke // 2, y_l - A_stroke // 2,
                          x_l + A_stroke // 2, y_l + A_stroke // 2], fill=AMBER)
            draw.ellipse([x_r - A_stroke // 2, y_r - A_stroke // 2,
                          x_r + A_stroke // 2, y_r + A_stroke // 2], fill=AMBER)

    # Crossbar with a stencil gap in the middle
    bar_y = 76
    draw.rectangle([52, bar_y - 3, 60, bar_y + 3], fill=AMBER)
    draw.rectangle([68, bar_y - 3, 76, bar_y + 3], fill=AMBER)

    img = add_glow(img, blur=3, opacity=0.45)
    save_png(img, "a1-bracketed-stencil-A.png")


# ============================================================
# A2 — L-Bracket Scope (4 corner brackets + center phosphor dot)
# ============================================================
def candidate_a2():
    img = Image.new("RGB", (SIZE, SIZE), IRON)
    draw = ImageDraw.Draw(img)

    arm = 30
    stroke = 6
    inset = 22

    # Top-left
    draw.rectangle([inset, inset, inset + stroke, inset + arm], fill=AMBER)
    draw.rectangle([inset, inset, inset + arm, inset + stroke], fill=AMBER)
    # Top-right
    draw.rectangle([SIZE - inset - stroke, inset, SIZE - inset, inset + arm], fill=AMBER)
    draw.rectangle([SIZE - inset - arm, inset, SIZE - inset, inset + stroke], fill=AMBER)
    # Bottom-left
    draw.rectangle([inset, SIZE - inset - arm, inset + stroke, SIZE - inset], fill=AMBER)
    draw.rectangle([inset, SIZE - inset - stroke, inset + arm, SIZE - inset], fill=AMBER)
    # Bottom-right
    draw.rectangle([SIZE - inset - stroke, SIZE - inset - arm, SIZE - inset, SIZE - inset], fill=AMBER)
    draw.rectangle([SIZE - inset - arm, SIZE - inset - stroke, SIZE - inset, SIZE - inset], fill=AMBER)

    # Center phosphor dot + small crosshair extending into the iron field
    cx, cy = SIZE // 2, SIZE // 2
    r_outer = 14
    r_inner = 8
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], fill=AMBER_DEEP)
    draw.ellipse([cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner], fill=AMBER)

    # Crosshair ticks
    draw.rectangle([cx - 1, cy - r_outer - 6, cx + 1, cy - r_outer + 2], fill=AMBER)
    draw.rectangle([cx - 1, cy + r_outer - 2, cx + 1, cy + r_outer + 6], fill=AMBER)
    draw.rectangle([cx - r_outer - 6, cy - 1, cx - r_outer + 2, cy + 1], fill=AMBER)
    draw.rectangle([cx + r_outer - 2, cy - 1, cx + r_outer + 6, cy + 1], fill=AMBER)

    img = add_glow(img, blur=4, opacity=0.5)
    save_png(img, "a2-scope-bracket-dot.png")


# ============================================================
# A3 — Dot-matrix "A" (looks like an MFD digital readout)
# ============================================================
def candidate_a3():
    img = Image.new("RGB", (SIZE, SIZE), IRON)
    draw = ImageDraw.Draw(img)

    A_glyph = [
        "0011100",
        "0010100",
        "0100010",
        "0100010",
        "1000001",
        "1111111",
        "1000001",
        "1000001",
        "1000001",
    ]

    cols = 7
    rows = 9
    dot_size = 11
    spacing = 13
    grid_w = cols * spacing
    grid_h = rows * spacing
    origin_x = (SIZE - grid_w) // 2 + spacing // 2
    origin_y = (SIZE - grid_h) // 2 + spacing // 2

    for ry, row in enumerate(A_glyph):
        for cx, ch in enumerate(row):
            if ch == "1":
                x = origin_x + cx * spacing
                y = origin_y + ry * spacing
                draw.ellipse([x - dot_size // 2, y - dot_size // 2,
                              x + dot_size // 2, y + dot_size // 2], fill=AMBER)

    img = add_glow(img, blur=5, opacity=0.6)
    save_png(img, "a3-mfd-dot-matrix-A.png")


if __name__ == "__main__":
    candidate_a1()
    candidate_a2()
    candidate_a3()
    print("\n3 candidates written to icons/candidates/")
