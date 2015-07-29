"""
Title : Design a Simple Automaton (Finite State Machine)

Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states,
q1, q2, and q3.

q1 is our start state. We begin reading commands from here.
q2 is our accept state. We return true if this is our last state.

q1 moves to q2 when given a 1, and stays at q1 when given a 0.
q2 moves to q3 when given a 0, and stays at q2 when given a 1.
q3 moves to q2 when given a 0 or 1.

Our automaton should return whether we end in our accepted state, or not (true/false.)
"""

import unittest


class Automaton(object):
    def __init__(self):
        self.states = []
        self.automata = {
            (1, 1): 2,
            (1, 0): 1,
            (2, 1): 2,
            (2, 0): 3,
            (3, 1): 2,
            (3, 0): 2,
        }

    def read_commands(self, commands):
        current_state = 1

        for command in commands:
            current_state = self.automata[(current_state, int(command))]
            self.states.append((int(command), current_state))

        return self.__is_accept_state(current_state)

    def __is_accept_state(self, state):
        return state == 2


my_automaton = Automaton()


class TestAutomaton(unittest.TestCase):
    def test_automaton_is_valid(self):
        automaton = Automaton()

        self.assertTrue(automaton.read_commands(['1']))
        self.assertTrue(automaton.read_commands(['1', '0', '0', '1']))
        self.assertFalse(automaton.read_commands(['1', '0', '0', '1', '0']))
