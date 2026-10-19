# Lab 02 – Zadanie 2 (★): Konwerter temperatury
#
# 1. Wczytaj temperaturę w stopniach Celsjusza i wypisz ją w Fahrenheitach:
#        F = C * 9 / 5 + 32
# 2. Wczytaj temperaturę w stopniach Fahrenheita i wypisz ją w Celsjuszach:
#        C = (F - 32) * 5 / 9
#
# Przykład: 37 °C = 98.6 °F,  212 °F = 100.0 °C
# Wyniki zaokrąglij do 1 miejsca po przecinku: f"{x:.1f}"

# TODO: Twój kod poniżej

celsius = float(input("Podaj temperaturę w °C: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:g} °C = {fahrenheit:.1f} °F")

fahrenheit = float(input("Podaj temperaturę w °F: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit:g} °F = {celsius:.1f} °C")
