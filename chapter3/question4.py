"""Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
- Time Complexity: enqueue, O(n), dequeue, O(1)
- Space Complexity: O(n)
"""
class QueueUsingStacks:
    def __init__(self):
        self.stack_ready = []
        self.stack_reorder = []
        
    def enqueue(self, data):
        while self.stack_ready:
            self.stack_reorder.append(self.stack_ready.pop())
        self.stack_ready.append(data)
        while self.stack_reorder:
            self.stack_ready.append(self.stack_reorder.pop())
            
    def dequeue(self):
        return self.stack_ready.pop()
    
import unittest

class Test(unittest.TestCase):
    def test(self):
        q = QueueUsingStacks()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())
        q.enqueue(1)
        q.dequeue()
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 2)