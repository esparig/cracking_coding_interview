"""Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        curr_min = self.min()
        if not curr_min or data < curr_min:
            curr_min = data 
        self.stack.append((data, curr_min))
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()[0]
    
    def min(self):
        if len(self.stack) > 0:
            return self.stack[-1][1]
        
import unittest

MYSTACK = Stack()
MYSTACK.push(1)
MYSTACK.push(2)
MYSTACK.push(0)

class TestStack(unittest.TestCase):
    def test(self):
        self.assertEqual(MYSTACK.min(), 0)
        self.assertEqual(MYSTACK.pop(), 0)
        self.assertEqual(MYSTACK.min(), 1)