# Lab 02 – Zadanie 4 (★): Sekundy na godziny, minuty i sekundy
#
# Program wczytuje liczbę sekund (int) i wypisuje ją DOKŁADNIE w formacie:
#     1 h 2 min 5 s
# (dla 3725 sekund).
#
# Wskazówki:
#   - int(input(...)) – konwersja tekstu na liczbę całkowitą
#   - // dzielenie całkowite, % reszta z dzielenia
#   - 1 h = 3600 s, 1 min = 60 s

# TODO: Twój kod poniżej

total_seconds = int(input("Podaj liczbę sekund: "))

hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 60

print(f"{hours} h {minutes} min {seconds} s")
