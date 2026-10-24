# Lab 06 – Zadanie 3 (★): Szyfr słownikowy (szyfr Cezara)
#
# Zbuduj SŁOWNIK, który każdej literze a–z przypisuje literę o 3 pozycje dalej:
#     {"a": "d", "b": "e", ..., "x": "a", "y": "b", "z": "c"}
# oraz słownik odwrotny do deszyfrowania.
#
# Program wczytuje tryb ("s" – szyfruj, "d" – deszyfruj) i tekst.
# Tekst zamień na małe litery; znaki spoza a–z (spacje, cyfry, ą, ę…) przepisz bez zmian.
#     s, "Ala ma kota"   ->  dod pd nrwd
#
# Wskazówki: alfabet masz w stałej ALPHABET; indeks (i + SHIFT) % 26 „zawija” alfabet.

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
SHIFT = 3

# TODO: Twój kod poniżej

encrypt = {}
decrypt = {}
for i in range(len(ALPHABET)):
    letter = ALPHABET[i]
    shifted = ALPHABET[(i + SHIFT) % 26]
    encrypt[letter] = shifted
    decrypt[shifted] = letter

mode = input("Tryb (s – szyfruj, d – deszyfruj): ").strip().lower()
text = input("Tekst: ").lower()

table = encrypt if mode == "s" else decrypt
result = ""
for char in text:
    result += table.get(char, char)

print(result)