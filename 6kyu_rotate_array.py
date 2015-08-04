"""
Title : Rotate Array (JS)

Note: This kata is a translation of this (Java) one: http://www.codewars.com/kata/rotate-array. I have not translated this first one as usual because I did not solved it, and I fear not being able to solve it (Java is not my cup of... tea). @cjmcgraw, if you want to use my translation on your kata feel free to use it.
Create a function named "rotate" that takes an array and returns a new one with the elements inside rotated n spaces.

If n is greater than 0 it should rotate the array to the right. If n is less than 0 it should rotate the array to the left. If n is 0, then it should return the array unchanged.

Example:

data = [1, 2, 3, 4, 5];

rotate(data, 1) # => [5, 1, 2, 3, 4]
rotate(data, 2) # => [4, 5, 1, 2, 3]
rotate(data, 3) # => [3, 4, 5, 1, 2]
rotate(data, 4) # => [2, 3, 4, 5, 1]
rotate(data, 5) # => [1, 2, 3, 4, 5]

rotate(data, 0) # => [1, 2, 3, 4, 5]

rotate(data, -1) # => [2, 3, 4, 5, 1]
rotate(data, -2) # => [3, 4, 5, 1, 2]
rotate(data, -3) # => [4, 5, 1, 2, 3]
rotate(data, -4) # => [5, 1, 2, 3, 4]
rotate(data, -5) # => [1, 2, 3, 4, 5]
Furthermore the method should take ANY array of objects and perform this operation on them:

rotate(['a', 'b', 'c'], 1)     # => ['c', 'a', 'b']
rotate([1.0, 2.0, 3.0], 1)     # => [3.0, 1.0, 2.0]
rotate([True, True, False], 1) # => [False, True, True]
Finally the rotation shouldn't be limited by the indices available in the array. Meaning that if we exceed the indices of the array it keeps rotating.

Example:

data = [1, 2, 3, 4, 5]

rotate(data, 7)     # => [4, 5, 1, 2, 3]
rotate(data, 11)    # => [5, 1, 2, 3, 4]
rotate(data, 12478) # => [3, 4, 5, 1, 2]
"""

import unittest

def rotate(arr, n):
    rotate_count = n % len(arr)
    return arr[len(arr) - rotate_count:] + arr[:len(arr) - rotate_count]


class TestRotate(unittest.TestCase):
    def test_rotate_is_valid(self):
        data = [1, 2, 3, 4, 5]
        self.assertListEqual([5, 1, 2, 3, 4], rotate(data, 1))
        self.assertListEqual([4, 5, 1, 2, 3], rotate(data, 2))
        self.assertListEqual([3, 4, 5, 1, 2], rotate(data, 3))
        self.assertListEqual([2, 3, 4, 5, 1], rotate(data, 4))
        self.assertListEqual([1, 2, 3, 4, 5], rotate(data, 5))

