"""
Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]
"""

import unittest


def flatten(lst):
    result = []

    for v in lst:
        if isinstance(v, list):
            result.extend(v)
        else:
            result.append(v)

    return result


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertListEqual(flatten([]), [], "[]")
        self.assertListEqual(flatten([1, 2, 3]), [1, 2, 3], "[1,2,3]")
        self.assertListEqual(flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]]), [1, 2, 3, "a", "b", "c", 1, 2, 3],
                             '[[1,2,3],["a","b","c"],[1,2,3]]')
        self.assertListEqual(flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3], "a"]),
                             [1, 2, 3, "a", "b", "c", 1, 2, 3, "a"],
                             '[[1,2,3],["a","b","c"],[1,2,3],"a"]')
        self.assertListEqual(flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]), [3, 4, 5, [9, 9, 9], "a,b,c"],
                             '[[3,4,5],[[9,9,9]],["a,b,c"]]')
        self.assertListEqual(flatten([[[3], [4], [5]], [9], [9], [8], [[1, 2, 3]]]),
                             [[3], [4], [5], 9, 9, 8, [1, 2, 3]],
                             '[[3,4,5],[[9,9,9]],["a,b,c"]]')
