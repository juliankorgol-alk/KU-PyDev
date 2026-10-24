"""Lab 13 – Zadanie 2 (★): Wyszukiwanie liniowe i binarne."""


def linear_search(values, target):
    """Indeks PIERWSZEGO wystąpienia target albo -1. Przeglądaj elementy po kolei (bez index())."""
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def binary_search(sorted_values, target):
    """Indeks target w POSORTOWANEJ liście albo -1 – wyszukiwanie binarne w pętli while.

        low, high = 0, len(sorted_values) - 1
        while low <= high:
            middle = (low + high) // 2
            ...
    Nie używaj index() ani in – testy liczą, ile elementów odczytasz (dla miliona: najwyżej 25).
    """
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        middle = (low + high) // 2
        value = sorted_values[middle]
        if value == target:
            return middle
        if value < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def binary_search_steps(sorted_values, target):
    """Ile obrotów pętli wykonało wyszukiwanie binarne (niezależnie od tego, czy znalazło)."""
    steps = 0
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        steps += 1
        middle = (low + high) // 2
        value = sorted_values[middle]
        if value == target:
            break
        if value < target:
            low = middle + 1
        else:
            high = middle - 1
    return steps