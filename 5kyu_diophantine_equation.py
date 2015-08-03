"""
Title : Diophantine Equation

In mathematics, a Diophantine equation is a polynomial equation, usually in two or more unknowns, such that only the integer solutions are sought or studied.

In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form

 x ^ 2 - 4 * y ^ 2 = A
where the unknowns are x and y (positive integers) and A a given positive number. Solutions x, y will be given as an array of arrays (Ruby, Python, Clojure)

 [[x1, y1], [x2, y2] ....]
as an array of tuples (Haskell)

 [(x1, y1), (x2, y2) ....]
and as a string (Java, C#)

 "[[x1, y1], [x2, y2] ....]"
in decreasing order of the positive xi. If there is no solution returns [] or "[]".

Example:

Hint: x ^ 2 - 4 y ^ 2 = (x - 2y) (x + 2y).
"""

import unittest
import math

def sol_equa(n):
    """
    x - 2y = first_num
    x + 2y = second_num
    """

    result = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i != 0:
            continue

        j = n / i
        y = (j - i) / 4
        x = i + 2 * y

        if x >= 0 and y >= 0 and (j == x + 2 * y) and (i == x - 2 * y):
            result.append([x, y])

    return sorted(result, reverse=True)


class TestDiophantineEquation(unittest.TestCase):
    def test_diophantine_equation_is_valud(self):
        self.assertListEqual(sol_equa(17), [[9, 4]])
        self.assertListEqual(sol_equa(12), [[4, 1]])
        self.assertListEqual(sol_equa(13), [[7, 3]])
        self.assertListEqual(sol_equa(16), [[4, 0]])
        self.assertListEqual(sol_equa(90005), [[45003, 22501], [9003, 4499], [981, 467], [309, 37]])
