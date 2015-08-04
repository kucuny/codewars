"""
Title : Last digit of a large number

Define a function

def last_digit(n1, n2):
  return
that takes in two numbers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.

The inputs to your function will always be non-negative integers.

Examples

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 4
Remarks

JavaScript

Since JavaScript doesn't have native arbitrary large integers, your arguments are going to be strings representing non-negative integers, e.g.

lastDigit("10", "10000000000");
The kata is still as hard as the variants for Haskell or Python, don't worry.
"""

import unittest


def last_digit(n1, n2):
    return pow(n1, n2, 10)


class TestLastDigitNumber(unittest.TestCase):
    def test_last_digit_number_is_valid(self):
        self.assertEqual(4, last_digit(4, 1))
        self.assertEqual(6, last_digit(4, 2))
        self.assertEqual(9, last_digit(9, 7))
        self.assertEqual(0, last_digit(10, 1000000000))
        self.assertEqual(6, last_digit(38710248912497124917933333333284108412048102948908149081409204712406,
                                       226628148126342643123641923461846128214626))
