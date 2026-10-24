"""Lab 12 – Zadanie 5 (☆, dodatkowe): Walidator numeru PESEL z hierarchią wyjątków.

PESEL: RRMMDDPPPPK
  - cyfra kontrolna K = (10 - (Σ cyfra_i · waga_i) mod 10) mod 10, wagi 1,3,7,9,1,3,7,9,1,3
  - miesiąc koduje stulecie: 1–12 -> 1900, 21–32 -> 2000, 41–52 -> 2100, 61–72 -> 2200, 81–92 -> 1800
  - 10. cyfra: parzysta -> kobieta ("K"), nieparzysta -> mężczyzna ("M")
"""
from datetime import date

WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


class PeselError(ValueError):
    """Bazowy wyjątek dla błędnego numeru PESEL."""


# TODO: zdefiniuj PeselLengthError, PeselDigitsError, PeselChecksumError dziedziczące po PeselError
class PeselLengthError(PeselError):
    """Numer PESEL ma złą długość."""


class PeselDigitsError(PeselError):
    """Numer PESEL zawiera znaki inne niż cyfry."""


class PeselChecksumError(PeselError):
    """Cyfra kontrolna się nie zgadza."""


def validate(pesel):
    """Zwraca True albo zgłasza odpowiedni wyjątek (długość, cyfry, suma kontrolna)."""
    if len(pesel) != 11:
        raise PeselLengthError(f"PESEL musi mieć 11 cyfr, ma {len(pesel)}")
    for char in pesel:
        if char not in "0123456789":
            raise PeselDigitsError("PESEL może zawierać tylko cyfry")
    total = 0
    for digit, weight in zip(pesel, WEIGHTS):
        total += int(digit) * weight
    if (10 - total % 10) % 10 != int(pesel[10]):
        raise PeselChecksumError("Błędna cyfra kontrolna")
    return True


def birth_date(pesel):
    """Data urodzenia zakodowana w numerze."""
    validate(pesel)
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    centuries = {0: 1900, 20: 2000, 40: 2100, 60: 2200, 80: 1800}
    offset = month // 20 * 20
    return date(centuries[offset] + year, month - offset, day)


def sex(pesel):
    """ "K" albo "M"."""
    validate(pesel)
    return "K" if int(pesel[9]) % 2 == 0 else "M"