"""Objętości brył."""
import math


def sphere_volume(r):
    """Objętość kuli: 4/3 · π · r³."""
    return 4 / 3 * math.pi * r ** 3


def cuboid_volume(a, b, c):
    """Objętość prostopadłościanu."""
    return a * b * c


def cylinder_volume(r, h):
    """Objętość walca: π · r² · h."""
    return math.pi * r ** 2 * h
