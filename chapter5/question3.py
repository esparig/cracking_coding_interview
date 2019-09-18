"""Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.
EXAMPLE
Input: 1775 (or: 11011101111)
Output: 8
- Time Complexity = O(n)
- Space Complexity = O(1)
"""
def flip_bit_win(num: int) -> int:
    x, count_ones, cur_ones, max_ones  = 1, 0, 0, 0
    while x < num:
        if x & num == x:
            count_ones += 1
        else:
            if max_ones < cur_ones + count_ones:
                max_ones = cur_ones + count_ones
            cur_ones = count_ones
            count_ones = 0
        x = x << 1
    return max_ones
    
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(flip_bit_win(1775), 8) # 11011101111
        self.assertTrue(flip_bit_win(3535), 6) # 110111001111
