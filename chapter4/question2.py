"""Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
- Time complexity: O(n) ??????
"""
from typing import List

class Node:
    def __init__(self, data: int, left: 'Node'=None, right: 'Node'=None):
        self.data = data
        self.left = left
        self.right = right

def minimal_tree(arr: List[int]):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return Node(arr[0])
    mid = len(arr)//2
    return Node(arr[mid], minimal_tree(arr[:mid]), minimal_tree(arr[mid+1:]))

tree = minimal_tree([1, 2, 3, 4, 5, 6])
print(tree.data, tree.left.data, tree.right.data)