"""Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
def all_unique_chars_using_set(string: str) -> bool:
    """Determine if a string has all unique characters using a set.
    - Computational cost: O(n)
    - Spatial cost: O(n)
    """
    visited_char = set()
    for char in string:
        if char in visited_char:
            return False
        visited_char.add(char)
    return True

def all_unique_chars_using_bit_vector(string: str) -> bool:
    """Determine if a string has all unique characters using a bit vector.
    - Computational cost: O(n)
    - Spatial cost: O(1)
    """
    visited_char = 0
    for char in string:
        if visited_char >> ord(char) & 1:
            return False
        visited_char = 1 << ord(char) | visited_char
    return True

def all_unique_chars(string: str) -> bool:
    """Determine if a string has all unique characters without using additional data structures.
    - Computational cost: O(n^2)
    - Spatial cost: O(1)
    """
    for idx, char1 in enumerate(string):
        for char2 in string[idx+1:]:
            if char1 == char2:
                return False
    return True

"""Other ideas:
- sort the string and look for repeated chars together: O(n log n)/O(1) if we alter the original string, if not O(n).
"""
        
import unittest

class Test1(unittest.TestCase):
    def tests(self):
        self.assertTrue(all_unique_chars("abc"))
        self.assertTrue(all_unique_chars_using_set("abc"))
        self.assertTrue(all_unique_chars_using_bit_vector("abc"))
        
        self.assertFalse(all_unique_chars("aba"))
        self.assertFalse(all_unique_chars_using_set("aba"))
        self.assertFalse(all_unique_chars_using_bit_vector("aba"))
