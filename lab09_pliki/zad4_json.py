"""Lab 09 – Zadanie 4 (★): Książka adresowa zapisywana w JSON.

Kontynuacja labu 06: słownik imię -> telefon przeżywa teraz zamknięcie programu.
"""
import json


def save_contacts(contacts, path):
    """Zapisuje słownik do pliku JSON.

    Użyj json.dump(..., ensure_ascii=False, indent=2), żeby polskie litery były czytelne.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def load_contacts(path):
    """Wczytuje słownik z pliku JSON; gdy pliku nie ma – zwraca {}."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def add_contact(path, name, phone):
    """Wczytuje kontakty, dodaje/nadpisuje jeden i zapisuje z powrotem."""
    contacts = load_contacts(path)
    contacts[name] = phone
    save_contacts(contacts, path)