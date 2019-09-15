"""Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.
- Sort only the keys, rearrange strings.
"""
from typing import List
from collections import defaultdict

def group_anagrams(arr_strings: List[str])->List[str]:
    d = defaultdict(list)
    for s in arr_strings:
        d["".join(sorted(s))].append(s)
    return [string for group in d.values() for string in group]

print(group_anagrams(["abc", "aba", "cba", "baa", "aab"]))