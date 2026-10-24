"""Lab 09 – Zadanie 1 (★): Logowanie zdarzeń do pliku.

Każdy wpis to jedna linia:  2026-12-08 09:15:02 | treść komunikatu
"""
from datetime import datetime


def log(message, path):
    """Dopisuje na KOŃCU pliku linię "RRRR-MM-DD GG:MM:SS | message".

    Wskazówki:
      - tryb "a" (append) dopisuje, "w" by nadpisał plik!
      - datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      - zawsze podawaj encoding="utf-8"
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {message}\n")


def read_log(path):
    """Zwraca listę wpisów (bez znaków końca linii). Brak pliku -> pusta lista.

    Wskazówka: pathlib.Path(path).exists() albo try/except FileNotFoundError.
    """
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def count_entries(path):
    """Liczba wpisów w logu."""
    return len(read_log(path))