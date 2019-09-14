"""Remove Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
1) No extra buffer:
- Time Complexity: O(n^2)
- Space Complexity: O(1)
2) Using an additional DS to store nodes
- Time complexity: O(n)
- Space complexity: O(n)
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

def remove_node(node: Node, parent: Node):
    parent.next = node.next

def remove_dups(linked_list: Node):
    if not linked_list:
        pass
    
    pointer1 = linked_list
    while pointer1 and pointer1.next:
        pointer2_parent = pointer1
        pointer2 = pointer1.next
        while pointer2:    
            if pointer1.value == pointer2.value:
                remove_node(pointer2, pointer2_parent)
            else:
                pointer2_parent  = pointer2_parent.next
            pointer2 = pointer2.next
        pointer1 = pointer1.next
        
def remove_dups_using_set(linked_list: Node):
    if not linked_list:
        pass
    
    dups = set()
    pointer = linked_list
    dups.add(pointer)
    
    while pointer.next:
        if pointer.next in dups:
            pointer.next = pointer.next.next
        else:
            dups.add(pointer.next)
            pointer = pointer.next
    
import unittest

LL1 = create_linked_list([2, 1, 1, 2, 3, 4, 3, 2])
LL2 = create_linked_list([2, 2])
LL3 = create_linked_list([2])

class Test(unittest.TestCase):
    
    def test_first_solution(self):
        remove_dups(LL1)
        self.assertEqual("2 -> 1 -> 3 -> 4", LL1.to_string())
        remove_dups(LL2)
        self.assertEqual("2", LL2.to_string())
        remove_dups(LL3)
        self.assertEqual("2", LL3.to_string())
        
    def test_second_solution(self):
        remove_dups_using_set(LL1)
        self.assertEqual("2 -> 1 -> 3 -> 4", LL1.to_string())
        remove_dups_using_set(LL2)
        self.assertEqual("2", LL2.to_string())
        remove_dups_using_set(LL3)
        self.assertEqual("2", LL3.to_string())
