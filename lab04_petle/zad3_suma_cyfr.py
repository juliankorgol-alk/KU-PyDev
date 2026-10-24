# Lab 04 – Zadanie 3 (★): Suma i liczba cyfr
#
# Program wczytuje nieujemną liczbę całkowitą i wypisuje DOKŁADNIE:
#     Suma cyfr: 15
#     Liczba cyfr: 5
# (dla 12345).
#
# Rozwiąż to ARYTMETYCZNIE pętlą while, bez zamiany na tekst:
#   - n % 10 to ostatnia cyfra,
#   - n // 10 „odcina” ostatnią cyfrę.
# Uwaga: liczba 0 ma jedną cyfrę.

# TODO: Twój kod poniżej

n = int(input("Podaj nieujemną liczbę całkowitą: "))

digit_sum = 0
digit_count = 0

while True:
    digit_sum += n % 10
    digit_count += 1
    n //= 10
    if n == 0:
        break

print(f"Suma cyfr: {digit_sum}")
print(f"Liczba cyfr: {digit_count}")
