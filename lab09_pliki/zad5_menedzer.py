"""Lab 09 – Zadanie 5 (☆, dodatkowe): Menedżer plików (pathlib)."""
from pathlib import Path


def find_by_extension(folder, extension):
    """Posortowana lista NAZW plików z danym rozszerzeniem (bez względu na wielkość liter).

    Wskazówki: Path(folder).iterdir(), p.is_file(), p.suffix.lower(), p.name
    """
    extension = extension.lower()
    if not extension.startswith("."):
        extension = "." + extension
    return sorted(p.name for p in Path(folder).iterdir() if p.is_file() and p.suffix.lower() == extension)


def organize(folder):
    """Przenosi pliki do podfolderów nazwanych od rozszerzenia (małymi literami, bez kropki).

    Pliki bez rozszerzenia trafiają do folderu "inne".
    Zwraca słownik: nazwa_podfolderu -> liczba przeniesionych plików.
    Wskazówki: (folder / "txt").mkdir(exist_ok=True), p.rename(nowa_ścieżka)
    """
    folder = Path(folder)
    summary = {}
    for p in list(folder.iterdir()):
        if not p.is_file():
            continue
        subfolder = p.suffix.lower().lstrip(".") or "inne"
        (folder / subfolder).mkdir(exist_ok=True)
        p.rename(folder / subfolder / p.name)
        summary[subfolder] = summary.get(subfolder, 0) + 1
    return summary