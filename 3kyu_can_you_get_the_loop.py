"""
Title : Can you get the loop ?

You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.
Image and video hosting by TinyPic

# Use the `next' attribute to get the following node

node.next
"""

import unittest

class Node:
    def __init__(self):
        pass

    def next(self):
        pass


def loop_size(node):
    current_count = 0
    current_node = node
    visited_node = {}
    visited_node[current_node] = current_count

    while True:
        if current_node.next in visited_node:
            return current_count - visited_node[current_node.next] + 1
        else:
            current_node = current_node.next
            current_count += 1
            visited_node[current_node] = current_count


class TestLoopSize(unittest.TestCase):
    def test_loop_size_is_valid(self):
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        self.assertEqual(3, loop_size(node1))
