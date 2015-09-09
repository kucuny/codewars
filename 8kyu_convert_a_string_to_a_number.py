"""
Title : Convert a String to a Number!

Description:

Note: This kata is inspired by Convert a Number to a String!. Try that one too.

Description

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples

stringToNumber("1234") == 1234
stringToNumber("605" ) == 605
stringToNumber("1405") == 1405
stringToNumber("-7"  ) == -7
"""

import unittest


def string_to_number(s):
    return int(s)


class TestStringToNumber(unittest.TestCase):
    def test_string_to_number_is_valid(self):
        self.assertEqual(1234, string_to_number("1234"))
        self.assertEqual(605, string_to_number("605"))
        self.assertEqual(1405, string_to_number("1405"))
        self.assertEqual(-7, string_to_number("-7"))
