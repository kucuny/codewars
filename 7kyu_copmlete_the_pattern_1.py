"""
Title : Complete The Pattern #1

Task:

You have to write a function pattern which returns the following Pattern(See Pattern & Examples) upto n number of rows.

Note:Returning the pattern is not the same as Printing the pattern.
Rules/Note:

If n < 1 then it should return "" i.e. empty string.
There are no whitespaces in the pattern.
Pattern:

1
22
333
....
.....
nnnnnn
"""

import unittest

def pattern(n):
    result = ''

    for i in xrange(n):
        for j in xrange(i + 1):
            result += str(i + 1)

        if i < n - 1:
            result += '\n'

    return result


class TestPattern(unittest.TestCase):
    def test_pattern_is_valid(self):
        self.assertEqual(pattern(1), '1')
        self.assertEqual(pattern(2), '1\n22')
        self.assertEqual(pattern(3), '1\n22\n333')
        self.assertEqual(pattern(5), '1\n22\n333\n4444\n55555')
