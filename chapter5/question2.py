"""Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR"
"""
import math

def print_bin(num: float):
    if num >= 1:
        print("ERROR")
    pos = 1
    binary_repr = ["0"]*32
    while num and pos <= 32:
        num *= 2
        if num >= 1:
            binary_repr[pos-1] = "1"
            num = math.modf(num)[0]
        pos += 1
    if pos > 33:
        print("ERROR")
    else:
        print("."+"".join(binary_repr))
        
print_bin(0.5625)
print_bin(0.9999999999)