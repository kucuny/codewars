"""
Title : Infix to Postfix Converter

Construct a function that, when given a string containing an expression in infix notation, will return an identical expression in postfix notation.

The operators used will be +, -, *, /, and ^ with standard precedence rules and left-associativity of all operators but ^.

The operands will be single-digit integers between 0 and 9, inclusive.

Parentheses may be included in the input, and are guaranteed to be in correct pairs.

to_postfix("2+7*5") # Should return "275*+"
to_postfix("3*3/(7+1)") # Should return "33*71+/"
to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"
You may read more about postfix notation, also called Reverse Polish notation, here: http://en.wikipedia.org/wiki/Reverse_Polish_notation
"""

import unittest


class Converter:
    op = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    def __init__(self, infix):
        self.infix = infix
        self.infix_list = list(infix)
        self.op_stack = []
        self.res_postfix = ''
        self.current_op = ''

    def to_postfix(self):
        res = ''

        if len(self.infix_list):
            return ''

        for op in self.infix_list:
            self.__calc_op(op)

        return res

    def __calc_op(self, op):
        if op not in self.op:
            self.res += self.res
        elif op == '(':
            pass
        elif op == ')':
            pass
        else:



def to_postfix(infix):
    conv = Converter(infix)
    res = conv.to_postfix()

    return res


class TestConverter(unittest.TestCase):
    def test_infix_to_postfix_is_valid(self):
        self.assertEqual('275*+', to_postfix('2+7*5'))
        self.assertEqual('33*71+/', to_postfix('3*3/(7+1)'))
        self.assertEqual('562-9*+371-^+', to_postfix('5+(6-2)*9+3^(7-1)'))
