# Lab 05 – Zadanie 1 (★): Lista zakupów
#
# Program w pętli wczytuje polecenia (każde w osobnej linii):
#     dodaj <produkt>   – dopisuje produkt na koniec listy (append)
#     usuń <produkt>    – usuwa produkt (remove); jeśli go nie ma:
#                         "Nie ma takiego produktu"
#     sortuj            – sortuje listę alfabetycznie (sort)
#     pokaż             – wypisuje produkty po przecinku, np.  masło, mleko
#                         albo "Lista jest pusta"
#     koniec            – kończy program
#
# Wskazówki:
#   - command, _, item = line.partition(" ")  dzieli linię na polecenie i resztę
#   - ", ".join(lista) skleja elementy listy w jeden tekst

shopping = []

# TODO: Twój kod poniżej

while True:
    line = input("Polecenie: ").strip()
    command, _, item = line.partition(" ")

    if command == "dodaj":
        shopping.append(item)
    elif command == "usuń":
        if item in shopping:
            shopping.remove(item)
        else:
            print("Nie ma takiego produktu")
    elif command == "sortuj":
        shopping.sort()
    elif command == "pokaż":
        if shopping:
            print(", ".join(shopping))
        else:
            print("Lista jest pusta")
    elif command == "koniec":
        break
