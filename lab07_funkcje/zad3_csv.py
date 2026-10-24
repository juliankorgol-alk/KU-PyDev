"""Lab 07 – Zadanie 3 (★): Analiza danych z pliku CSV.

Plik dane/oceny.csv ma nagłówek:  imie,nazwisko,ocena
Ocena studenta to krotka ("Imię Nazwisko", ocena_float).
"""
import csv


def load_grades(path):
    """Wczytuje plik CSV i zwraca listę krotek, np. [("Anna Kowalska", 4.5), ...].

    Wskazówka:
        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                row["imie"], row["nazwisko"], row["ocena"]
    """
    grades = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            grades.append((f"{row['imie']} {row['nazwisko']}", float(row["ocena"])))
    return grades


def average(grades):
    """Średnia ocen; dla pustej listy zwraca 0.0."""
    if not grades:
        return 0.0
    return sum(grade for _, grade in grades) / len(grades)


def best(grades):
    """Zwraca krotkę studenta z najwyższą oceną (przy remisie – pierwszego z listy)."""
    return max(grades, key=lambda student: student[1])


def count_passing(grades, threshold=3.0):
    """Ile ocen jest >= threshold. Parametr ma wartość domyślną 3.0."""
    count = 0
    for _, grade in grades:
        if grade >= threshold:
            count += 1
    return count


def main():
    grades = load_grades("dane/oceny.csv")
    print(f"Liczba studentów: {len(grades)}")
    print(f"Średnia: {average(grades):.2f}")
    print(f"Najlepszy wynik: {best(grades)}")
    print(f"Zaliczyło: {count_passing(grades)}")


if __name__ == "__main__":
    main()