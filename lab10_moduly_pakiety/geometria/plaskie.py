"""Pola figur płaskich."""
import math


def circle_area(r):
    """Pole koła o promieniu r (użyj math.pi)."""
    return math.pi * r ** 2


def rectangle_area(a, b):
    """Pole prostokąta a × b."""
    return a * b


def triangle_area(a, b, c):
    """Pole trójkąta ze wzoru Herona: p = (a+b+c)/2,  P = sqrt(p(p-a)(p-b)(p-c)).

    Gdy z boków nie da się zbudować trójkąta, zwraca None.
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return None
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
