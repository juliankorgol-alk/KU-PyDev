"""Lab 13 – Zadanie 5 (☆, dodatkowe): Sortowanie przez wstawianie i przez scalanie."""


def insertion_sort(values):
    """Jak układanie kart w dłoni: każdy kolejny element wstaw we właściwe miejsce posortowanej części."""
    result = list(values)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def merge_sort(values):
    """Dziel i zwyciężaj: podziel na połowy, posortuj rekurencyjnie, scal dwie posortowane listy. O(n log n)."""
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged