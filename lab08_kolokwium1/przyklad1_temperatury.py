# Kolokwium I – PRZYKŁAD 1 (skrypt): Statystyka temperatur
#
# Program wczytuje temperatury (float), każdą w osobnej linii, do pustej linii.
# Wypisuje DOKŁADNIE:
#     Min: -2.5
#     Max: 5.5
#     Średnia: 1.00
#     Dni z mrozem: 2          <- temperatury < 0
# Jeśli nie podano żadnej temperatury: "Brak danych"

# TODO: Twój kod poniżej

temperatures = []

while True:
    line = input("Temperatura (Enter kończy): ").strip()
    if line == "":
        break
    temperatures.append(float(line))

if not temperatures:
    print("Brak danych")
else:
    frost_days = 0
    for temp in temperatures:
        if temp < 0:
            frost_days += 1
    print(f"Min: {min(temperatures)}")
    print(f"Max: {max(temperatures)}")
    print(f"Średnia: {sum(temperatures) / len(temperatures):.2f}")
    print(f"Dni z mrozem: {frost_days}")