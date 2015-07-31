"""
Title : Molecule to atoms

For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object.

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
"""

import unittest
import re

def parse_molecule(fomula):
    if fomula == '':
        return {}

    temp_res = []

    inner_regexp = re.compile('([\(\[\{]((?:[A-Z][a-z]?\d*)+)[\)\]\}](\d*))')
    sub_regexp = re.compile('([A-Z][a-z]?)(\d*)')

    inner_matches = inner_regexp.findall(fomula)
    while len(inner_matches) > 0:
        for match in inner_matches:
            sub_matches = sub_regexp.findall(match[1])

            count = 1
            if match[2] != '':
                count = int(match[2])

            for sub_match in sub_matches:
                sub_count = 1
                if sub_match[1] != '':
                    sub_count = int(sub_match[1])

                temp_res.append((sub_match[0], sub_count * count))

            temp_elem = []
            for elem, count in temp_res:
                temp_elem.append(elem + str(count))

            fomula = fomula.replace(match[0], ''.join(temp_elem))
            temp_res = []

        inner_matches = inner_regexp.findall(fomula)

    sub_matches = sub_regexp.findall(fomula)
    for sub_match in sub_matches:
        sub_count = 1
        if sub_match[1] != '':
            sub_count = int(sub_match[1])

        temp_res.append((sub_match[0], sub_count))

    result = {}
    for elem, count in temp_res:
        if elem in result:
            result[elem] += count
        else:
            result[elem] = count

    return result


class TestParseMolecule(unittest.TestCase):
    def test_parse_molecule_is_valid(self):
        # self.assertDictEqual(parse_molecule("C6H12O6"), {})
        self.assertDictEqual(parse_molecule("(C5H5)Fe(CO)2CH3"), {'C': 8, 'H': 8, 'Fe': 1, 'O': 2})
        self.assertDictEqual(parse_molecule("K4[ON(SO3)2]2"), {'K': 4, 'O': 14, 'N': 2, 'S': 4})
        self.assertDictEqual(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O': 2, 'H': 2})
        self.assertDictEqual(parse_molecule("Mg2"), {'Mg': 2})
        self.assertDictEqual(parse_molecule("H2O"), {'H': 2, 'O': 1})
