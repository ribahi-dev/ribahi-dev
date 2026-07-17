from PIL import Image, ImageOps, ImageEnhance

SRC = r"C:\Users\elmeh\Desktop\CV\copi 1.jpeg"
RAMP = "@%#*+=-:. "  # dense -> sparse


def render(width=46, contrast=1.5, gamma=1.0, bottom_crop=0.16, char_aspect=0.5):
    img = Image.open(SRC).convert("L")

    w, h = img.size
    img = img.crop((0, 0, w, int(h * (1 - bottom_crop))))

    img = ImageOps.autocontrast(img, cutoff=2)
    img = ImageEnhance.Contrast(img).enhance(contrast)

    w, h = img.size
    height = max(1, int(width * (h / w) * char_aspect))
    img = img.resize((width, height), Image.LANCZOS)

    px = img.load()
    lines = []
    for y in range(height):
        row = []
        for x in range(width):
            v = pow(px[x, y] / 255.0, gamma)
            v = 1.0 - v  # dark pixels -> dense glyph
            row.append(RAMP[int((1.0 - v) * (len(RAMP) - 1) + 0.5)])
        lines.append("".join(row).rstrip())
    return lines


if __name__ == "__main__":
    lines = render()
    print("\n".join(lines))
    print()
    print("rows:", len(lines), "| max width:", max(len(l) for l in lines))
