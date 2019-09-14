"""Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""
from collections import Counter

def is_permutation(str1: str, str2: str) -> bool:
    """
    - Time complexity: O(n+m)
    - Space complexity: O(n+m)
    """
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

def is_permutation_less_space(str1: str, str2: str) -> bool:
    """
    - Time complexity: O(m+n)
    - Space complexity: O(m)
    """
    if len(str1) != len(str2):
        return False
    count_chars = {}
    for c in str1:
        if c in count_chars:
            count_chars[c] += 1
        count_chars[c] = 1
    for c in str2:
        if c not in count_chars or count_chars[c] < 1:
            return False
        count_chars[c] -= 1
    return True

def is_permutation_sorting(str1: str, str2: str) -> bool:
    """
    - Time complexity: O(n log n)
    - Space complexity: O(1)
    """
    return all(a == b for a, b in zip(sorted(list(str1)), sorted(list(str2))))

import unittest

class Test(unittest.TestCase):
    def test_solution1(self):
        self.assertTrue(is_permutation("abc", "bca"))
        self.assertFalse(is_permutation("abc", "baa"))
        
    def test_solution2(self):
        self.assertTrue(is_permutation_less_space("abc", "bca"))
        self.assertFalse(is_permutation_less_space("abc", "baa"))
        
    def test_solution3(self):
        self.assertTrue(is_permutation_sorting("abc", "bca"))
        self.assertFalse(is_permutation_sorting("abc", "baa"))
