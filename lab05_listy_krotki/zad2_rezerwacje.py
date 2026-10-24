# Lab 05 – Zadanie 2 (★): System rezerwacji miejsc
#
# Sala ma 5 rzędów i 8 miejsc w rzędzie (numeracja od 1).
# Miejsce to KROTKA (rząd, miejsce), np. (2, 5). Rezerwacje trzymaj na liście krotek.
#
# Polecenia:
#     rezerwuj R M  – "Zarezerwowano (R, M)"
#                     jeśli już zajęte: "Miejsce (R, M) jest zajęte"
#                     jeśli poza salą:  "Nie ma takiego miejsca"
#     anuluj R M    – usuwa rezerwację (albo "Brak takiej rezerwacji")
#     lista         – wypisuje POSORTOWANĄ listę rezerwacji, np. [(1, 1), (2, 5)]
#     wolne         – "Wolne miejsca: 38"
#     koniec
#
# Wskazówki:
#   - parts = line.split()  ->  ["rezerwuj", "2", "5"]
#   - seat = (int(parts[1]), int(parts[2]))
#   - print(sorted(reservations)) – krotki sortują się po kolei: najpierw rząd, potem miejsce

ROWS = 5
SEATS_PER_ROW = 8
reservations = []

# TODO: Twój kod poniżej

while True:
    parts = input("Polecenie: ").split()
    command = parts[0] if parts else ""

    if command in ("rezerwuj", "anuluj"):
        seat = (int(parts[1]), int(parts[2]))
        row, number = seat
        if command == "rezerwuj":
            if not (1 <= row <= ROWS and 1 <= number <= SEATS_PER_ROW):
                print("Nie ma takiego miejsca")
            elif seat in reservations:
                print(f"Miejsce {seat} jest zajęte")
            else:
                reservations.append(seat)
                print(f"Zarezerwowano {seat}")
        else:
            if seat in reservations:
                reservations.remove(seat)
                print(f"Anulowano {seat}")
            else:
                print("Brak takiej rezerwacji")
    elif command == "lista":
        print(sorted(reservations))
    elif command == "wolne":
        print(f"Wolne miejsca: {ROWS * SEATS_PER_ROW - len(reservations)}")
    elif command == "koniec":
        break
