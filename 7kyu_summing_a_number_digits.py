"""
Title : Summing a number's digits
Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:

  sumDigits(10)  # Returns 1
  sumDigits(99)  # Returns 18
  sumDigits(-32) # Returns 5

Let's assume that all numbers in the input will be integer values.

"""


def sum_digits(number):
    convert_str = str(abs(number))
    convert_list = list(convert_str)

    list_int = [int(v) for v in convert_list]

    return sum(list_int)

import unittest


class TestSumDigit(unittest.TestCase):
    def test_sum_digit(self):
        self.assertEqual(1, sum_digits(10))
        self.assertEqual(18, sum_digits(99))
        self.assertEqual(5, sum_digits(-32))
        self.assertEqual(11, sum_digits(56))
