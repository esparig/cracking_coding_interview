"""Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
"""
from typing import Any

class SetOfStacks:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.list_stacks = []
    
    def __len__(self):
        if self.list_stacks:
            return (len(self.list_stacks) - 1) * self.max_capacity + len(self.list_stacks[-1])
        return 0
    
    def __str__(self):
        return f"SetOfStacks(Max_capacity: {self.max_capacity}: {self.list_stacks})"
    
    def __repr__(self):
        return f"SetOfStacks(Max_capacity: {self.max_capacity}: {self.list_stacks})"
    
    def push(self, data: Any):
        if len(self.list_stacks) == 0 or len(self.list_stacks[-1]) == self.max_capacity:
            self.list_stacks.append([data])
        else:
            self.list_stacks[-1].append(data)
            
    def pop(self) -> Any:
        if len(self.list_stacks) > 0:
            data_to_pop = self.list_stacks[-1].pop()
            if len(self.list_stacks[-1]) == 0:
                self.list_stacks.pop()
            return data_to_pop
        return None
    
    def pop_at(self, idx: int) -> Any:
        return self.list_stacks[idx].pop()
    
import unittest
   
class Test(unittest.TestCase):
    def test_push(self):
        stack = SetOfStacks(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.__repr__(), "SetOfStacks(Max_capacity: 2: [[1, 2], [3, 4], [5]])")
        
    def test_pop(self):
        stack = SetOfStacks(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)
        
    def test_pop_at(self):
        stack = SetOfStacks(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop_at(2), 5)
        self.assertEqual(stack.pop_at(1), 4)
        self.assertEqual(stack.pop_at(0), 2)
