"""
Q1. Strange Equality

Given an integer A.
Two numbers, X and Y, are defined as follows:

X is the greatest number smaller than A such that the XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A, such that the XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.

NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.
NOTE 2: Your code will be run against a maximum of 100000 Test Cases.
"""


def solve(A):
    x = 0
    y = 0
    tmp = A
    i = 0
    while tmp:
        if tmp & 1 == 0:
            x += (1 << i)
        i += 1
        tmp >>= 1

    y = 1 << i
    return x ^ y


if __name__ == '__main__':
    print(solve(5))
