"""Lab 11 – Zadanie 5 (☆, dodatkowe): Kalendarz."""
from datetime import date, timedelta

DAYS = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]


def weekday_name(day):
    """Polska nazwa dnia tygodnia. Wskazówka: day.weekday() zwraca 0 dla poniedziałku."""
    return DAYS[day.weekday()]


def is_weekend(day):
    """Czy to sobota albo niedziela?"""
    return day.weekday() >= 5


def working_days(start, end):
    """Liczba dni roboczych (pon–pt) od start do end WŁĄCZNIE (bez uwzględniania świąt)."""
    count = 0
    day = start
    while day <= end:
        if not is_weekend(day):
            count += 1
        day += timedelta(days=1)
    return count