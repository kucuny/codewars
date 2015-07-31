"""
Title : Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior")

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")
"""

import unittest
import re


def to_camel_case(text):
    if text == '':
        return ''

    regexp = re.compile('([-|_](\S))')

    match = regexp.findall(text)

    for source, replace in match:
        text = text.replace(source, replace.upper())

    return text


class TestToCamelCase(unittest.TestCase):
    def test_convert_string_to_camel_case_is_valid(self):
        self.assertEqual(to_camel_case(''), '')
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior")
        self.assertEqual(to_camel_case("A-B-C"), "ABC")
