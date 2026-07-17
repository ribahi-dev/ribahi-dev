# -*- coding: utf-8 -*-
"""Charge le dessin ASCII depuis art.txt (une ligne = une ligne du dessin)."""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def render(*_args, **_kwargs):
    """Renvoie le dessin comme liste de lignes (droite non rognee)."""
    path = os.path.join(_HERE, "art.txt")
    with open(path, encoding="utf-8") as f:
        lines = [line.rstrip("\n").rstrip() for line in f]
    while lines and lines[-1] == "":
        lines.pop()
    return lines
