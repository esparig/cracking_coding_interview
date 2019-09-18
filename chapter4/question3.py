"""List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
- Time complexity: O(n)
- Space complexity: O(n)
"""
from typing import List, Any
from collections import deque

class NodeTree:
    def __init__(self, data: int, left: 'Node'=None, right: 'Node'=None):
        self.data = data
        self.left = left
        self.right = right
        
class Node:
    def __init__(self, data: int, next: 'Node'=None):
        self.data = data
        self.next = next
        
    def to_string(self):
        node = self
        values = []
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values)
    
def create_linked_list(values: List[Any]) -> Node:
    if len(values) > 0:
        return Node(values[0], create_linked_list(values[1:]))
    return None

def create_linked_lists_from_binary_tree(tree: NodeTree) -> List[Node]:
    q, aux_list = deque(), []
    q.append(tree)
    yield Node(tree.data)
    while True:
        while q:
            node = q.popleft()
            if node.left:
                aux_list.append(node.left)
            if node.right:
                aux_list.append(node.right)
        if len(aux_list) == 0:
            break
        yield create_linked_list([node.data for node in aux_list])
        q.extend(aux_list)
        aux_list.clear()

import unittest

class Test(unittest.TestCase):
    def test(self):
        tree = NodeTree(1, NodeTree(2, NodeTree(4), NodeTree(5)), NodeTree(3, NodeTree(6, NodeTree(8)), NodeTree(7)))
        """
                 1
               /   \
              2     3
            /  \   / \
           4    5 6   7
                /
               8
        """
        generator = create_linked_lists_from_binary_tree(tree)
        self.assertTrue(next(generator).to_string(), "1")
        self.assertTrue(next(generator).to_string(), "2 -> 3")
        self.assertTrue(next(generator).to_string(), "4 -> 5 -> 6 -> 7")
        self.assertTrue(next(generator).to_string(), "8")
