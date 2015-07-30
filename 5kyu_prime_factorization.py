"""
Title : Prime factorization

The prime factorization of a positive integer is a list of the integer's prime factors, together with their multiplicities; the process of determining these factors is called integer factorization. The fundamental theorem of arithmetic says that every positive integer has a single unique prime factorization.

The prime factorization of 24, for instance, is (2^3) * (3^1).

Without using the prime library, write a class called PrimeFactorizer that takes in an integer greater than 1 and has a method called factor which returns a hash where the keys are prime numbers and the values are the multiplicities.

PrimeFactorizer(24).factor #should return { 2: 3, 3: 1 }
"""

import unittest


class PrimeFactorizer:
    def __init__(self, number):
        self.number = number
        self.factor = self.__get_factor

    @property
    def __get_factor(self):
        factor_result = {}
        init_value = 2
        while init_value <= self.number:
            count = 0
            while (self.number % init_value) == 0:
                self.number /= init_value
                count += 1

            if count > 0:
                factor_result[init_value] = count

            init_value += 1

        return factor_result


class TestPrimeFactorizer(unittest.TestCase):
    def test_prime_factorizer_is_valid(self):
        self.assertDictEqual(PrimeFactorizer(13).factor, {13: 1})
        self.assertDictEqual(PrimeFactorizer(24).factor, {2: 3, 3: 1})