"""Lab 12 – Zadanie 2 (★): Walidacja danych wejściowych."""


def parse_age(text):
    """Zamienia tekst na wiek (int). Zgłasza ValueError z komunikatem, gdy:
        - to nie jest liczba całkowita   -> "Wiek musi być liczbą całkowitą"
        - wiek < 0                       -> "Wiek nie może być ujemny"
        - wiek > 150                     -> "Wiek nie może przekraczać 150 lat"

    Wskazówka:  raise ValueError("...")   (a int() sam zgłasza ValueError dla "abc" –
    złap go i zgłoś własny, czytelny komunikat)
    """
    try:
        age = int(text)
    except ValueError:
        raise ValueError("Wiek musi być liczbą całkowitą") from None
    if age < 0:
        raise ValueError("Wiek nie może być ujemny")
    if age > 150:
        raise ValueError("Wiek nie może przekraczać 150 lat")
    return age


def read_int(prompt, low, high, input_func=input, output=print):
    """Pyta (input_func(prompt)) tak długo, aż użytkownik poda liczbę całkowitą z przedziału [low, high].

    Po złej odpowiedzi wypisuje (output(...)):
        "Podaj liczbę całkowitą"           – gdy to nie liczba
        "Wartość spoza zakresu 1–10"       – gdy liczba poza zakresem (z low i high)
    Zwraca poprawną liczbę.

    Parametry input_func i output pozwalają testom podstawić atrapy zamiast klawiatury i ekranu.
    """
    while True:
        try:
            value = int(input_func(prompt))
        except ValueError:
            output("Podaj liczbę całkowitą")
            continue
        if low <= value <= high:
            return value
        output(f"Wartość spoza zakresu {low}–{high}")


if __name__ == "__main__":
    print(read_int("Ocena (1–10): ", 1, 10))