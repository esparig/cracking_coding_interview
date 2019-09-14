"""Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
- Time complexity: O(3^n)
- Space complexity: recursion stack / O(n) using lru_cache
"""
import functools

@functools.lru_cache()
def stairs(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n > 0:
        return stairs(n-1)+stairs(n-2)+stairs(n-3)
    
import unittest

class Test(unittest.TestCase):
    def tearDown(self):
        print(stairs.cache_info())
        stairs.cache_clear()
        
    def test(self):
        self.assertEqual(stairs(3), 4)
        
    def test2(self):
        self.assertEqual(stairs(4), 7)
        
    def test3(self):
        print(stairs(100))
