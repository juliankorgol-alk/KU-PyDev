# Lab 06 – Zadanie 1 (★): Książka adresowa
#
# Kontakty trzymaj w SŁOWNIKU: imię -> numer telefonu.
#
# Polecenia (każde w osobnej linii):
#     dodaj <imię> <telefon>  – dodaje albo nadpisuje kontakt, "Zapisano <imię>"
#     szukaj <imię>           – wypisuje numer albo "Brak kontaktu"
#     usuń <imię>             – usuwa kontakt albo "Brak kontaktu"
#     lista                   – wszystkie kontakty ALFABETYCZNIE, każdy w linii:  Adam: 500600700
#     koniec
#
# Wskazówki: contacts.get(name), del contacts[name], sorted(contacts.items())

contacts = {}

# TODO: Twój kod poniżej

while True:
    parts = input("Polecenie: ").split()
    command = parts[0] if parts else ""

    if command == "dodaj":
        name, phone = parts[1], parts[2]
        contacts[name] = phone
        print(f"Zapisano {name}")
    elif command == "szukaj":
        print(contacts.get(parts[1], "Brak kontaktu"))
    elif command == "usuń":
        name = parts[1]
        if name in contacts:
            del contacts[name]
            print(f"Usunięto {name}")
        else:
            print("Brak kontaktu")
    elif command == "lista":
        for name, phone in sorted(contacts.items()):
            print(f"{name}: {phone}")
    elif command == "koniec":
        break