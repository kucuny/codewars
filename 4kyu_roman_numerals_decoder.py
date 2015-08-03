"""
Title : Roman Numerals Decoder

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21
C# RomanDecode.Solution("XXI") -- should return 21
"""

import unittest

CONVERT_ROMAN_CHAR = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def solution(roman):
    result = 0
    prev_num = CONVERT_ROMAN_CHAR['M']
    for c in roman:
        conv = CONVERT_ROMAN_CHAR[c]
        if conv <= prev_num:
            result += conv
            prev_num = conv
        else:
            result -= 2 * prev_num
            result += conv

    return result


class TestRomanNumeralsDecoder(unittest.TestCase):
    def test_roman_numerals_decoder_is_valid(self):
        self.assertEqual(21, solution('XXI'))
        self.assertEqual(1, solution('I'))
        self.assertEqual(29, solution('XXIX'))
        self.assertEqual(50, solution('L'))
        self.assertEqual(530, solution('DXXX'))
        self.assertEqual(707, solution('DCCVII'))
