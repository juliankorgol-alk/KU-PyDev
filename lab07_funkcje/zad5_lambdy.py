"""Lab 07 – Zadanie 5 (☆, dodatkowe): Funkcje jako argumenty, lambdy i zasięg."""

counter = 0


def apply_to_all(func, values):
    """Zwraca nową listę: func zastosowana do każdego elementu values."""
    return [func(value) for value in values]


def sort_by_last_name(names):
    """Sortuje listę "Imię Nazwisko" po nazwisku – użyj sorted(..., key=lambda ...)."""
    return sorted(names, key=lambda name: name.split()[-1])


def filter_even(numbers):
    """Zwraca listę liczb parzystych – użyj filter() i lambdy."""
    return list(filter(lambda number: number % 2 == 0, numbers))


def increment():
    """Zwiększa zmienną GLOBALNĄ counter o 1 (słowo kluczowe global)."""
    global counter
    counter += 1
    return counter