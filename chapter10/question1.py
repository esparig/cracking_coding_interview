"""Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
- Time complexity: one single bisect: O(log n), is done m times = O(m log n)
"""
from typing import List
import bisect

def merge_sorted_arrays_using_bisect(long_arr: List[int], short_arr: List[int]):
    shift = len(short_arr)
    end = len(long_arr)+shift
    while shift:
        insert = bisect.bisect_right(long_arr[:end], short_arr[shift-1])
        long_arr = long_arr[:insert] + [short_arr[shift-1]] + long_arr[insert:]
        shift -= 1
        end = insert
    return long_arr

def merge_sorted_arrays(long_arr: List[int], n: int, short_arr: List[int], m: int):
    write = n + m - 1
    i, j = n - 1, m - 1
    while j >= 0:
        if long_arr[i] > short_arr[j]:
            long_arr[write] = long_arr[i]
            i -= 1
        else:
            long_arr[write] = short_arr[j]
            j -= 1
        write -= 1
    return long_arr

import unittest
import time

class SomeTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print(f"{self.id()}, {t}")

    def testOne(self):
        for _ in range(100000):
            self.assertEquals(merge_sorted_arrays([1, 2, 4, 5, 6, 8, 9, None, None], 7, [3, 7], 2), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def testTwo(self):
        for _ in range(100000):
            self.assertEquals(merge_sorted_arrays_using_bisect([1, 2, 4, 5, 6, 8, 9], [3, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
            
"""
chapter10.question1.SomeTest.testOne, 0.7067711353302002
chapter10.question1.SomeTest.testTwo, 0.753751277923584
----------------------------------------------------------------------
Ran 2 tests in 1.461s

OK
"""

