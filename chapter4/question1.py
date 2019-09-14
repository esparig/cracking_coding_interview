"""Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
BFS finds the shortest path when there is one.
- Time complexity: O(k^d)
- Space complexity: O(n)
"""
from collections import deque

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = []
        
def has_route(node1: Node, node2: Node):
    visited = set()
    q = deque()
    q.append(node1)
    while q:
        node = q.popleft()
        visited.add(node)
        for next_node in node.next:
            if next_node == node2:
                return True
            if next_node not in visited:
                q.append(next_node)
    return False