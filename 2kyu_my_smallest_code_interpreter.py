"""
Title : My smallest code interpreter (aka Brainf**k)

Inspired from real-world Brainf**k, we want to create an interpreter of that language which will support the following instructions (the machine memory or 'data' should behave like a potentially infinite array of bytes, initialized to 0):

> increment the data pointer (to point to the next cell to the right).
< decrement the data pointer (to point to the next cell to the left).
+ increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
- decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
. output the byte at the data pointer.
, accept one byte of input, storing its value in the byte at the data pointer.
[ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
The function will take in input...

the program code, a string with the sequence of machine instructions,
the program input, a string, eventually empty, that will be interpreted as an array of bytes using each character's ASCII code and will be consumed by the , instruction
... and will return ...

the output of the interpreted code (always as a string), produced by the . instruction.
"""

import unittest


def brain_luck(code, input):
    brain = BrainFuck(code, input)

    is_success = brain.run()

    if is_success:
        return brain.output()



class BrainFuck:
    def __init__(self, code, input_data):
        self.code = list(code)
        self.code_index = 0
        self.input_index = 0
        self.input_data = list(input_data)
        self.output_data = []
        self.cells = [0]
        self.pointer = 0

        self.BRAINFUCK_CODE_LIST = {
            '>': self.__increment_data_pointer,
            '<': self.__decrement_data_pointer,
            '+': self.__increment_the_byte,
            '-': self.__decrement_the_byte,
            '.': self.__output_the_byte,
            ',': self.__get_byte_from_input_data,
            '[': self.__start_loop,
            ']': self.__end_loop,

        }

        self.MAX_NUMBER = 255
        self.MIN_NUMBER = 0

        self.bracket_list = {}

    def run(self):
        self.__parse_the_code()

        try:
            while self.code_index < len(self.code):
                current_code = self.code[self.code_index]
                self.BRAINFUCK_CODE_LIST[current_code]()

                if current_code not in ('[', ']'):
                    self.code_index += 1

            return True
        except Exception, e:
            print(e)
            return False

    def output(self):
        return ''.join([c for c in self.output_data])

    def __parse_the_code(self):
        stack_bracket = []
        for i in xrange(len(self.code)):
            if self.code[i] == '[':
                stack_bracket.append((i, 0))
            elif self.code[i] == ']':
                temp = stack_bracket.pop()
                self.bracket_list[temp[0]] = i
                self.bracket_list[i] = temp[0]

    def __increment_data_pointer(self):
        self.cells.append(0)
        self.pointer += 1

    def __decrement_data_pointer(self):
        self.pointer -= 1

    def __increment_the_byte(self):
        if self.cells[self.pointer] == self.MAX_NUMBER:
            self.cells[self.pointer] = self.MIN_NUMBER
        else:
            self.cells[self.pointer] += 1

    def __decrement_the_byte(self):
        if self.cells[self.pointer] == self.MIN_NUMBER:
            self.cells[self.pointer] = self.MAX_NUMBER
        else:
            self.cells[self.pointer] -= 1

    def __output_the_byte(self):
        self.output_data.append(chr(self.cells[self.pointer]))

    def __get_byte_from_input_data(self):
        self.cells[self.pointer] = ord(self.input_data[self.input_index])
        self.input_index += 1

    def __start_loop(self):
        if self.cells[self.pointer] == 0:
            index = self.code_index
            self.code_index = self.bracket_list[index] + 1
        else:
            self.code_index += 1

    def __end_loop(self):
        if self.cells[self.pointer] == 0:
            self.code_index += 1
        else:
            self.code_index = self.bracket_list[self.code_index]


class TestBrainFuck(unittest.TestCase):
    def test_brain_fuck_is_valid(self):
        self.assertEqual('C', brain_luck(',.', 'Codewars'))
        self.assertEqual('D', brain_luck(',+.', 'Codewars'))
        self.assertEqual('c', brain_luck(',,,-.', 'Codewars'))
        self.assertEqual('Codewars', brain_luck(',+[-.,+]', 'Codewars' + chr(255)))
        self.assertEqual(chr(72), brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))
        self.assertEqual('Codewars', brain_luck(',[.[-],]', 'Codewars' + chr(0)))
