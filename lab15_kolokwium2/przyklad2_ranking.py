"""Kolokwium II – PRZYKŁAD 2: sortowanie i wyszukiwanie (bez sorted() w rank)."""


def rank(results):
    """Nowa lista krotek (imię, punkty) – malejąco po punktach, przy remisie alfabetycznie.

    Napisz sortowanie przez wstawianie; nie używaj sorted() ani list.sort().
    """
    result = list(results)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        # (−punkty, imię): mniejszy klucz = wyżej w rankingu
        while j >= 0 and (-result[j][1], result[j][0]) > (-current[1], current[0]):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def find(sorted_names, name):
    """Wyszukiwanie binarne imienia w posortowanej liście; indeks albo -1."""
    low, high = 0, len(sorted_names) - 1
    while low <= high:
        middle = (low + high) // 2
        current = sorted_names[middle]
        if current == name:
            return middle
        if current < name:
            low = middle + 1
        else:
            high = middle - 1
    return -1