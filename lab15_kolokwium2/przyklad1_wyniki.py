"""Kolokwium II – PRZYKŁAD 1: pliki i wyjątki.

Plik CSV z liniami  imię;punkty  (np. "Ala;45").
"""


class ScoresFileError(Exception):
    """Zgłaszany, gdy pliku z wynikami nie ma. Komunikat zawiera ścieżkę pliku."""


def load_scores(path):
    """Zwraca krotkę (słownik imię -> punkty jako float, liczba_błędnych_linii).

    Puste linie pomija bez liczenia; linie bez ";" albo z punktami, które nie są liczbą – liczy jako błędne.
    Brak pliku -> ScoresFileError(f"Brak pliku: {path}").
    """
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        raise ScoresFileError(f"Brak pliku: {path}") from None

    scores = {}
    errors = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ";" not in line:
            errors += 1
            continue
        name, _, points = line.partition(";")
        try:
            scores[name.strip()] = float(points)
        except ValueError:
            errors += 1
    return scores, errors