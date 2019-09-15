"""URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""
from typing import List

def urlify(address: str) -> str:
    return "%20".join(address.strip().split(" "))

def urlify_in_place(address:List[str], n: int) -> str:
    # first pass: count spaces
    num_spaces = 0
    for write_idx in range(n):
        if address[write_idx] == " ":
            num_spaces += 1
    # second pass: rearrange chars
    write_idx = n+2*num_spaces-1
    cur_idx = n - 1
    while write_idx >= 0:
        if address[cur_idx] == ' ':
            address[write_idx-2:write_idx+1] = '%20'
            write_idx -= 3
        else:
            address[write_idx] = address[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return "".join(address)
            
    
print(urlify("Mr John Smith "))
print(urlify_in_place(["M", "r", " ", "J", "o", "h", "n", " ", "S", "m", "i", "t", "h", " ", " ", " ", " "], 13))
