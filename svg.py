# -*- coding: utf-8 -*-
"""Generate a coloured neofetch-style SVG (renders in colour on GitHub)."""
import re
from html import escape
from artload import render

# ---- palette (matches the neofetch look) ----
BG      = "#0d1117"
ART     = "#7ee787"   # green portrait
LABEL   = "#58a6ff"   # blue labels
VALUE   = "#c9d1d9"   # near-white values
DOTS    = "#30363d"   # faint dot leaders
HEADER  = "#d29922"   # amber headers/dashes
ACCENT  = "#f778ba"   # pink for @handle

CH_W    = 8.4         # px per character (monospace advance)
LINE_H  = 17          # px per line
FONT    = 14          # px
PAD     = 22
INFO_W  = 56
GAP     = 3

# ---- info card model: (kind, *parts) ----
INFO = [
    ("header", "elmehdi@ribahi-dev"),
    ("field", "OS", "Windows 11, Linux"),
    ("field", "Host", "EMSI - Ecole Marocaine des Sciences"),
    ("field", "Kernel", "Ingenierie Informatique & Reseaux"),
    ("field", "IDE", "VS Code, IntelliJ IDEA"),
    ("blank",),
    ("field", "Languages.Programming", "TypeScript, Python, PHP, Java"),
    ("field", "Languages.Computer", "HTML, CSS, SQL, JSON, YAML"),
    ("field", "Languages.Real", "Francais, Arabe, Anglais"),
    ("blank",),
    ("field", "Hobbies.Software", "Web Dev, Open Source"),
    ("field", "Hobbies.Hardware", "<a completer>"),
    ("blank",),
    ("section", "Contact"),
    ("field", "Email.Personal", "elmehdi.ribahi@gmail.com"),
    ("field", "LinkedIn", "<ton-handle>"),
    ("field", "Discord", "<ton-handle>"),
    ("blank",),
    ("section", "GitHub Stats"),
    ("field", "Repos", "19"),
    ("field", "Following", "6"),
    ("field", "Stars", "<x>"),
]


def tspan(text, color, x=None):
    xa = f' x="{x:.1f}"' if x is not None else ""
    return f'<tspan{xa} fill="{color}">{escape(text)}</tspan>'


def info_line(item, x0):
    """Return a list of coloured tspans for one info row, plus its plain length."""
    kind = item[0]
    if kind == "blank":
        return "", 0
    if kind == "header":
        title = item[1]
        dashes = INFO_W - len(title) - 2
        s = tspan(title, ACCENT, x0) + tspan(" " + "-" * max(dashes, 1), HEADER)
        return s, INFO_W
    if kind == "section":
        title = item[1]
        dashes = INFO_W - len(title) - 4
        s = (tspan("- ", DOTS, x0) + tspan(title, HEADER)
             + tspan(" " + "-" * max(dashes, 1), DOTS))
        return s, INFO_W
    # field
    _, label, value = item
    dots = max(INFO_W - len(label) - 1 - len(value) - 2, 1)
    s = (tspan(label, LABEL, x0)
         + tspan(" " + "." * dots + " ", DOTS)
         + tspan(value, VALUE))
    return s, len(label) + 1 + dots + 1 + len(value)


def build():
    art = render(width=46)
    art_w = max(len(l) for l in art)
    n = max(len(art), len(INFO))

    height = n * LINE_H + PAD * 2
    width = int((art_w + GAP + INFO_W) * CH_W + PAD * 2)
    info_x = PAD + (art_w + GAP) * CH_W

    rows = []
    for i in range(n):
        y = PAD + FONT + i * LINE_H
        spans = []
        if i < len(art) and art[i].strip():
            spans.append(tspan(art[i], ART, PAD))
        if i < len(INFO):
            s, _ = info_line(INFO[i], info_x)
            if s:
                spans.append(s)
        if spans:
            rows.append(f'<text y="{y:.1f}">{"".join(spans)}</text>')

    body = "\n  ".join(rows)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
  <rect width="{width}" height="{height}" rx="10" fill="{BG}"/>
  <g font-family="'Cascadia Code','JetBrains Mono','DejaVu Sans Mono',Consolas,monospace" font-size="{FONT}px" xml:space="preserve">
  {body}
  </g>
</svg>
'''


if __name__ == "__main__":
    svg = build()
    with open("profile.svg", "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print("profile.svg written")
