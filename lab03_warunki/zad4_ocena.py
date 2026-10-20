# Lab 03 – Zadanie 4 (★): Ocena z przedmiotu
#
# Program wczytuje liczbę punktów (0–100) i wypisuje ocenę według progów
# z sylabusa naszego przedmiotu:
#     > 91        -> 5
#     > 83 – 91   -> 4.5
#     > 75 – 83   -> 4
#     > 67 – 75   -> 3.5
#     > 60 – 67   -> 3
#     <= 60       -> 2
#
# Przykład:  Ocena: 4.5
# Uwaga: w zachęcie input() nie wypisuj liczb (np. „0-100”) – testy szukają liczb w wyjściu.

# TODO: Twój kod poniżej

points = float(input("Podaj liczbę punktów: "))

if points > 91:
    grade = 5
elif points > 83:
    grade = 4.5
elif points > 75:
    grade = 4
elif points > 67:
    grade = 3.5
elif points > 60:
    grade = 3
else:
    grade = 2

print(f"Ocena: {grade}")
