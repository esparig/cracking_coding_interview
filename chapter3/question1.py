"""Three in One: Describe how you could use a single array to implement three stacks.
- Time complexity: peek, O(1); push, O(1); pop, O(1)
- Space complexity: O(n)
"""
class ThreeStacksFromAnArray:
    def __init__(self):
        self.stack = []
        self.peek_id = [None, None, None]
        self.next = 0
        
    def peek(self, id_stack):
        if self.peek_id[id_stack] != None:
            return self.stack[self.peek_id[id_stack]][0]
       
    def push(self, id_stack: int, value: int):
        self.stack.insert(self.next, (value, self.peek_id[id_stack]))
        self.peek_id[id_stack] = self.next
        self.next += 1
        
    def pop(self, id_stack):
        value, previous_peek = self.stack[self.peek_id[id_stack]]
        self.stack[self.peek_id[id_stack]] = self.stack[-1]
        self.peek_id[id_stack] = previous_peek
        return value

my_stack = ThreeStacksFromAnArray()
my_stack.push(0, 2)
my_stack.push(0, 3)
print("Peeks:", my_stack.peek(0), my_stack.peek(1), my_stack.peek(2))
print("Pop from 0:", my_stack.pop(0))
print("Peeks:", my_stack.peek(0), my_stack.peek(1), my_stack.peek(2))
my_stack.push(1, 4)
my_stack.push(2, 0)
print("Peeks:", my_stack.peek(0), my_stack.peek(1), my_stack.peek(2))
print("Pop from 1:", my_stack.pop(1))
print("Pop from 0:", my_stack.pop(0))
my_stack.push(1, 2)
print("Peeks:", my_stack.peek(0), my_stack.peek(1), my_stack.peek(2))
