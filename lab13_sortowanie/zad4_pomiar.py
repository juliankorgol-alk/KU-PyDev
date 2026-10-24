"""Lab 13 – Zadanie 4 (★): Eksperyment – jak rośnie czas sortowania?

Po uruchomieniu (python zad4_pomiar.py) uzupełnij w AI.md tabelę wyników i wnioski.
"""
import random
import time

from zad1_sortowania import bubble_sort, selection_sort


def time_function(sort_func, n, repeats=3):
    """NAJKRÓTSZY z `repeats` czasów sortowania losowej listy n liczb (time.perf_counter)."""
    best = None
    for _ in range(repeats):
        data = [random.random() for _ in range(n)]
        start = time.perf_counter()
        sort_func(data)
        elapsed = time.perf_counter() - start
        if best is None or elapsed < best:
            best = elapsed
    return best


def growth_ratio(sort_func, n):
    """Iloraz czasu dla 2n i dla n. Dla O(n²) spodziewaj się ok. 4, dla O(n log n) – nieco ponad 2."""
    return time_function(sort_func, 2 * n) / time_function(sort_func, n)


if __name__ == "__main__":
    print(f"{'n':>6} {'bąbelkowe':>12} {'wybieranie':>12} {'sorted()':>12}")
    for n in (500, 1000, 2000, 4000):
        row = [time_function(f, n) for f in (bubble_sort, selection_sort, sorted)]
        print(f"{n:>6} " + " ".join(f"{t:>12.5f}" for t in row))