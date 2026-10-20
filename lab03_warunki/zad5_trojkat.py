# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej

a = float(input("Podaj pierwszy bok: "))
b = float(input("Podaj drugi bok: "))
c = float(input("Podaj trzeci bok: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Nie da się zbudować trójkąta")
else:
    if a == b == c:
        kind = "równoboczny"
    elif a == b or b == c or a == c:
        kind = "równoramienny"
    else:
        kind = "różnoboczny"

    x, y, longest = sorted([a, b, c])
    if abs(x ** 2 + y ** 2 - longest ** 2) < 1e-9:
        kind += ", prostokątny"

    print(f"Trójkąt {kind}")
