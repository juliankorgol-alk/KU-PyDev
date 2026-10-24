"""Kolokwium I – PRZYKŁAD 2 (funkcje): Stan magazynu.

Stan magazynu to słownik: nazwa produktu -> liczba sztuk.
Funkcje zmieniają przekazany słownik (nie tworzą nowego).
"""


def add_stock(inventory, item, quantity):
    """Dodaje quantity sztuk produktu (nowy produkt też)."""
    inventory[item] = inventory.get(item, 0) + quantity


def remove_stock(inventory, item, quantity):
    """Zdejmuje quantity sztuk. Zwraca True, gdy się udało.

    Zwraca False (i NIC nie zmienia), gdy produktu brak albo jest go za mało.
    Gdy stan spada do 0 – usuń produkt ze słownika.
    """
    if inventory.get(item, 0) < quantity:
        return False
    inventory[item] -= quantity
    if inventory[item] == 0:
        del inventory[item]
    return True


def low_stock(inventory, threshold):
    """Zwraca posortowaną alfabetycznie listę produktów, których jest MNIEJ niż threshold."""
    return sorted(item for item, count in inventory.items() if count < threshold)