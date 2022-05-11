"""
Q1. Max Sum Contiguous Subarray

Problem Description
    Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
"""

import math


def maxSubArray(A):
    n = len(A)
    summ = -math.inf

    ps: list = [A[0]]
    for i in range(1, n):
        ps.append(ps[i - 1] + A[i])
    # print(ps)
    for i in range(n):
        for j in range(i, n):
            if j == 0 or i == 0:
                temp = ps[j]
            else:
                temp = ps[j] - ps[i - 1]
            summ = max(summ, temp)
            # print(temp)

    return summ


def maxSubArray_optimized(A):
    n = len(A)

    curr_sum = A[0]
    max_sum = A[0]

    for i in range(1, n):
        curr_sum = max(A[i], curr_sum + A[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == '__main__':
    # A = [1, 2, 3, 4, -10]
    print(maxSubArray_optimized([2, 9, 5]))
    print(maxSubArray_optimized([1, 2, 3, 4, -10]))
    print(maxSubArray_optimized([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray_optimized([-10, -10, -10, -10, -10]))
