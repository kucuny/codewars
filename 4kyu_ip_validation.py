"""
Title : IP Validation

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. Input to the function is guaranteed to be a single string.

Examples of valid inputs: 1.2.3.4 123.45.67.89

Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089
"""

import unittest
import re


def is_valid_IP(string):
    base_regexp = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    res = base_regexp.match(string)

    if res is None:
        return False

    sub = string.split('.')

    idx = 0
    for value in sub:
        if idx == 0 and value == '0':
            return False

        if idx > 0 and len(value) > 1 and value[0] == '0':
            return False

        if 0 < int(value) < 256:
            pass
        else:
            return False

        idx += 1

    return True


class TestIPValidation(unittest.TestCase):
    def test_ip_is_valid(self):
        self.assertTrue(is_valid_IP('12.255.56.1'))
        self.assertTrue(is_valid_IP('12.255.56.1'))
        self.assertTrue(is_valid_IP('12.255.56.1'))
        self.assertTrue(is_valid_IP('12.255.56.1'))
        self.assertTrue(is_valid_IP('12.255.56.1'))

    def test_ip_is_not_valid(self):
        self.assertFalse(is_valid_IP(''))
        self.assertFalse(is_valid_IP('abc.def.ghi.jkl'))
        self.assertFalse(is_valid_IP('12.34.56.-1'))
        self.assertFalse(is_valid_IP('12..56.1'))
        self.assertFalse(is_valid_IP('123.045.067.089'))
        self.assertFalse(is_valid_IP('1.222.0.161'))
