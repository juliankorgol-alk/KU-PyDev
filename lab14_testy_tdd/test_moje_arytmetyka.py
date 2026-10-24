"""Lab 14 – Zadanie 2 (★): TWOJE testy modułu arytmetyka.py.

Uruchom:  python -m unittest test_moje_arytmetyka -v

Wymagania (sprawdza tests/test_obowiazkowe.py):
  - co najmniej 8 metod testowych,
  - wszystkie przechodzą na poprawnym arytmetyka.py,
  - wykrywają 6 „mutantów” – kopii modułu z celowo wprowadzonym błędem (tests/mutanty/).

Testuj przypadki typowe I brzegowe: 0, 1, liczby ujemne, kwadraty liczb pierwszych, wyjątki.
"""
import unittest

from arytmetyka import factorial, gcd, is_prime, lcm


class TestGcd(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(gcd(12, 18), 6)

    def test_coprime(self):
        self.assertEqual(gcd(7, 13), 1)

    def test_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_negative(self):
        self.assertEqual(gcd(-12, 18), 6)
        self.assertEqual(gcd(12, -18), 6)


class TestLcm(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_coprime(self):
        self.assertEqual(lcm(3, 5), 15)

    def test_zero(self):
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)

    def test_negative(self):
        self.assertEqual(lcm(-4, 6), 12)


class TestIsPrime(unittest.TestCase):
    def test_below_two(self):
        for n in (-7, 0, 1):
            self.assertFalse(is_prime(n), n)

    def test_primes(self):
        for n in (2, 3, 5, 13, 97):
            self.assertTrue(is_prime(n), n)

    def test_squares_of_primes(self):
        for n in (4, 9, 25, 49, 121):
            self.assertFalse(is_prime(n), n)

    def test_other_composites(self):
        for n in (6, 15, 91):
            self.assertFalse(is_prime(n), n)


class TestFactorial(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_typical(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()