"""Lab 11 – Zadanie 3 (★): Statystyka opisowa z modułem math.

Napisz funkcje SAMODZIELNIE (bez modułu statistics) – testy porównają je ze statistics.
"""
import math


def mean(values):
    """Średnia arytmetyczna."""
    return sum(values) / len(values)


def median(values):
    """Mediana: środkowy element posortowanych danych, a dla parzystej liczby – średnia dwóch środkowych.

    NIE zmieniaj listy wejściowej (użyj sorted, nie sort).
    """
    ordered = sorted(values)
    n = len(ordered)
    middle = n // 2
    if n % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def std_dev(values):
    """Odchylenie standardowe z PRÓBY:  sqrt( Σ(x - średnia)² / (n - 1) ).  Użyj math.sqrt."""
    avg = mean(values)
    squares = sum((x - avg) ** 2 for x in values)
    return math.sqrt(squares / (len(values) - 1))