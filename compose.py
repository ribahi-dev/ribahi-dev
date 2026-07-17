# -*- coding: utf-8 -*-
"""Compose the neofetch-style profile README (ASCII art + right-hand info card)."""
import io
import re
from artload import render

ART_W = 42
GAP = 3
INFO_W = 56  # width of the info column, dots included

C = "[36m"   # cyan   - labels
W = "[37m"   # white  - values
G = "[32m"   # green
R = "[31m"   # red
Y = "[33m"   # yellow
B = "[34m"   # blue
D = "[90m"   # grey   - dot leaders
X = "[0m"    # reset

ANSI_RE = re.compile(r"\[[0-9;]*m")


def vislen(s):
    return len(ANSI_RE.sub("", s))


def field(label, value, vcolor=W):
    """label ....... value  — dot leaders, right-aligned value."""
    dots = INFO_W - len(label) - 1 - vislen(value) - 2
    dots = max(dots, 1)
    return f"{C}{label}{X} {D}{'.' * dots}{X} {vcolor}{value}{X}"


def header(title):
    dashes = INFO_W - len(title) - 2
    return f"{Y}{title}{X} {D}{'-' * max(dashes, 1)}{X}"


def section(title):
    dashes = INFO_W - len(title) - 4
    return f"{D}-{X} {Y}{title}{X} {D}{'-' * max(dashes, 1)}{X}"


INFO = [
    header("elmehdi@ribahi-dev"),
    field("OS", "Windows 11, Linux"),
    field("Host", "EMSI - Ecole Marocaine des Sciences"),
    field("Kernel", "Ingenierie Informatique & Reseaux"),
    field("IDE", "VS Code, IntelliJ IDEA"),
    "",
    field("Languages.Programming", "TypeScript, Python, PHP, Java"),
    field("Languages.Computer", "HTML, CSS, SQL, JSON, YAML"),
    field("Languages.Real", "Francais, Arabe, Anglais"),
    "",
    field("Hobbies.Software", "Web Dev, Open Source"),
    field("Hobbies.Hardware", "<a completer>"),
    "",
    section("Contact"),
    field("Email.Personal", "elmehdi.ribahi@gmail.com"),
    field("LinkedIn", "<ton-handle>"),
    field("Discord", "<ton-handle>"),
    "",
    section("GitHub Stats"),
    field("Repos", "19"),
    field("Following", "6"),
    field("Stars", "<x>"),
]


def main():
    art = render(width=ART_W)
    art_w = max((len(l) for l in art), default=0)
    n = max(len(art), len(INFO))

    out = io.StringIO()
    for i in range(n):
        left = art[i] if i < len(art) else ""
        right = INFO[i] if i < len(INFO) else ""
        pad = " " * (art_w - len(left) + GAP)
        out.write((left + pad + right).rstrip() + "\n")
    return out.getvalue()


if __name__ == "__main__":
    body = main()
    readme = "```ansi\n" + body + "```\n"
    with open("README.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(readme)
    print(body)
