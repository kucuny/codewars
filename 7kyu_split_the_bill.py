import unittest


def split_the_bill(x):
    avg = sum(x.values()) / float(len(x))
    return {key: round(value - avg, 2) for key, value in x.items()}


class TestSplitTheBill(unittest.TestCase):
    def test_split_the_bill_is_valid(self):
        self.assertDictEqual(split_the_bill({'A': 20, 'B': 15, 'C': 10}), {'A': 5, 'B': 0, 'C': -5})
        self.assertDictEqual(split_the_bill({'A': 40, 'B': 25, 'X': 10}), {'A': 15, 'B': 0, 'X': -15})
