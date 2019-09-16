"""Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""
class Node:
    def __init__(self, data: int, next: 'Node'):
        self.data = data
        self.next = next
        
    def to_string(self):
        node = self
        values = []
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values)

def create_linked_list(values):
    if len(values) > 0:
        return Node(values[0], create_linked_list(values[1:]))
    return None

def delete_midle(llist: Node):
    while llist.next.next:
        llist.data = llist.next.data
        llist = llist.next
    llist.data = llist.next.data
    llist.next = None

import unittest

LL1 = create_linked_list([1, 2, 3, 4, 5])

class Test(unittest.TestCase):
    
    def test_first_solution(self):
        delete_midle(LL1.next.next)
        self.assertEqual("1 -> 2 -> 4 -> 5", LL1.to_string())
