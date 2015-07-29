"""
Title : Check for prime numbers
In this kata you will create a function to check a non-negative input to see if it is a prime number.

The function will take in a number and will return True if it is a prime number and False if it is not.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Examples

isPrime(0) is false
isPrime(1) is false
isPrime(2) is true
isPrime(11) is true
isPrime(12) is false
"""


def is_prime(n):
    init_value = 2

    if n == init_value:
        return True

    if n < init_value:
        return False

    while init_value < n:
        mod_result = n % init_value

        if mod_result == 0:
            return False

        init_value += 1

    return True


from unittest import TestCase


class TestPrimeNumber(TestCase):
    def test_check_prime_number_is_valid(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(12))
        self.assertTrue(is_prime(571))
        self.assertFalse(is_prime(25))
