"""
Title : Prefill an Array

Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.

You have to validate input:

v can be anything (primitive or otherwise)
if v is ommited, fill the array with undefined
if n is 0, return an empty array
if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.

Code Examples

    prefill(3,1) --> [1,1,1]

    prefill(2,"abc") --> ['abc','abc']

    prefill("1", 1) --> [1]

    prefill(3, prefill(2,'2d'))
      --> [['2d','2d'],['2d','2d'],['2d','2d']]

    prefill("xyz", 1)
      --> throws TypeError with message "xyz is invalid"
"""

import unittest


def prefill(n, v=''):
    number = 0
    try:
        number = int(n)
    except:
        return TypeError("%s is invalid", str(n))

    result = []
    step = 0
    while step < number:
        result.append(v)
        step += 1

    return result


class TestPrefill(unittest.TestCase):
    def test_prefill_is_valid(self):
        try:
            prefill('asdf', 1)
        except Exception as err:
            self.assertEqual(type(err), TypeError)
            self.assertEqual(str(err), 'asdf is invalid')

        self.assertListEqual(prefill(0, 1), [])
        self.assertListEqual(prefill(3, 1), [1, 1, 1])
        self.assertListEqual(prefill(2, 'abc'), ['abc', 'abc'])
        self.assertListEqual(prefill('1', 1), [1])
        self.assertListEqual(prefill(3, prefill(2, '2d')), [['2d', '2d'], ['2d', '2d'], ['2d', '2d']])
