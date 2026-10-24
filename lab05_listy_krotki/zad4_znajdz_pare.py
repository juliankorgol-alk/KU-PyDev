# Lab 05 – Zadanie 4 (☆, dodatkowe): Gra „znajdź parę” (memory)
#
# Na stole leży 8 zakrytych kart (pozycje 0–7), po dwie z każdej litery.
# Gracz podaje dwie pozycje oddzielone spacją, np.  0 4
#   - jeśli karty są takie same: "Para!"  (karty zostają odkryte)
#   - jeśli różne: "Pudło"
#   - jeśli podał dwa razy tę samą pozycję: "Podaj dwie różne karty" (ruch się nie liczy)
# Po odkryciu wszystkich par: "Koniec gry w 5 ruchach"
#
# Przed każdym ruchem wypisz stół, np.:  ? ? A ? ? ? A ?
#
# Testy ustawiają BEZ_TASOWANIA, żeby układ kart był znany:

import os
import random

cards = ["A", "B", "C", "D", "A", "B", "C", "D"]
if "BEZ_TASOWANIA" not in os.environ:
    random.shuffle(cards)
revealed = [False] * len(cards)

# TODO: Twój kod poniżej

moves = 0

while False in revealed:
    table = []
    for i in range(len(cards)):
        table.append(cards[i] if revealed[i] else "?")
    print(" ".join(table))

    parts = input("Podaj dwie pozycje: ").split()
    first, second = int(parts[0]), int(parts[1])
    if first == second:
        print("Podaj dwie różne karty")
        continue

    moves += 1
    if cards[first] == cards[second]:
        revealed[first] = True
        revealed[second] = True
        print("Para!")
    else:
        print("Pudło")

print(f"Koniec gry w {moves} ruchach")
