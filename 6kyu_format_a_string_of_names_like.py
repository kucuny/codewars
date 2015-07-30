"""
Title : Format a string of names like 'Bart, Lisa & Maggie'.

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
"""

import unittest
import string

def namelist(names):
    name = []

    for n in names:
        name.append(n['name'])

    if len(name) < 2:
        return string.join(name, ', ')

    return string.join(name[:len(name) - 2] + [string.join(name[len(name) - 2:], ' & ')], ', ')

class TestNamelist(unittest.TestCase):
    def test_name_list_is_valid(self):
        self.assertEqual(namelist([]), '')
        self.assertEqual(namelist([{'name': 'Bart'}]), 'Bart')
        self.assertEqual(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]), 'Bart & Lisa')
        self.assertEqual(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie')
        self.assertEqual(
            namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]),
            'Bart, Lisa, Maggie, Homer & Marge')
