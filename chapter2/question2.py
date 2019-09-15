"""Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
- Time complexity: O(n)
- Space complexity: O(1)
"""
class Node:
    def __init__(self, value: int, next: 'Node'):
        self.value = value
        self.next = next
        
    def to_string(self):
        node = self
        values = []
        while node:
            values.append(str(node.value))
            node = node.next
        return " -> ".join(values)

def create_linked_list(values):
    if len(values) > 0:
        return Node(values[0], create_linked_list(values[1:]))
    return None

def kth_last(llist: Node, k: int) -> Node:
    p_to_end, p_to_k = llist, llist
    for _ in range(k):
        p_to_end = p_to_end.next
    while p_to_end:
        p_to_end, p_to_k = p_to_end.next, p_to_k.next
    return p_to_k

import unittest

LL = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])

class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(kth_last(LL, 1).value, 9)
        self.assertEqual(kth_last(LL, 3).value, 7)
        self.assertEqual(kth_last(LL, 5).value, 5)
