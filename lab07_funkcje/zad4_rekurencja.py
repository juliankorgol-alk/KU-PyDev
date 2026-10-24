"""Lab 07 – Zadanie 4 (★): Rekurencja.

Każdą funkcję napisz REKURENCYJNIE (funkcja wywołuje samą siebie), bez pętli.
Zawsze zacznij od warunku stopu (przypadku bazowego)!
"""


def factorial(n):
    """n! = n * (n-1)!, a 0! = 1."""
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base, exponent):
    """base ** exponent dla exponent >= 0, bez operatora **."""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def sum_digits(n):
    """Suma cyfr liczby n >= 0: ostatnia cyfra + suma cyfr reszty (n % 10, n // 10)."""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)