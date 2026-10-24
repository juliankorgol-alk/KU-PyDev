"""Lab 12 – Zadanie 4 (★): Własne wyjątki i asercje."""


class InsufficientFundsError(Exception):
    """Brak środków na koncie.

    TODO: dopisz __init__(self, balance, amount), który:
      - zapamięta self.balance i self.amount,
      - wywoła super().__init__(f"Brak środków: saldo {balance}, żądano {amount}")
    """

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Brak środków: saldo {balance}, żądano {amount}")


def withdraw(balance, amount):
    """Zwraca saldo po wypłacie.

    - amount <= 0       -> ValueError("Kwota musi być dodatnia")
    - amount > balance  -> InsufficientFundsError(balance, amount)
    """
    if amount <= 0:
        raise ValueError("Kwota musi być dodatnia")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


def percent(part, whole):
    """Jaki procent całości stanowi część.

    Na początku sprawdź ASERCJĄ, że whole > 0:
        assert whole > 0, "Całość musi być dodatnia"
    Asercje chronią przed błędami PROGRAMISTY, nie użytkownika.
    """
    assert whole > 0, "Całość musi być dodatnia"
    return part / whole * 100