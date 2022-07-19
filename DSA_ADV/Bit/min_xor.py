"""
Q2. Min XOR value

Given an integer array A of N integers,
find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.
"""


def findMinXor(A):
    n = len(A)
    # import math
    # ans = math.inf
    # for i in range(n):
    #     for j in range(i+1, n):
    #         ans = min(ans, A[i]^A[j])

    A.sort()
    min_xor = A[0] ^ A[1]
    for i in range(2, n):
        min_xor = min(min_xor, A[i - 1] ^ A[i])
    return min_xor
