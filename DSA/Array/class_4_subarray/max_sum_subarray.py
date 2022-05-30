"""
Q1. Max Sum Contiguous Subarray

Problem Description
    Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
"""

import math


def maxSubArray_1(A):
    # with prefix sum way
    # TC : O(n^2)
    # SC : O(N)
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


def maxSubArray(A):
    # with carry forward way
    # TC : O(n^2)
    # SC : O(1)
    n = len(A)
    ans_sum = -math.inf

    for i in range(n):
        tmp_sum = 0
        for j in range(i, n):
            tmp_sum += A[j]
            ans_sum = max(ans_sum, tmp_sum)
    return ans_sum


def maxSubArray_optimized(A):
    # kadane's algorithm
    # TC : O(N)
    # SC : O(1)
    n = len(A)

    curr_sum = A[0]
    max_sum = A[0]

    for i in range(1, n):
        curr_sum = max(A[i], curr_sum + A[i])
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


if __name__ == '__main__':
    # A = [1, 2, 3, 4, -10]
    print(maxSubArray([2, 9, 5]))
    print(maxSubArray_optimized([2, 9, 5]))

    print(maxSubArray([1, 2, 3, 4, -10]))
    print(maxSubArray_optimized([1, 2, 3, 4, -10]))

    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray_optimized([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    print(maxSubArray([-10, -10, -10, -10, -10]))
    print(maxSubArray_optimized([-10, -10, -10, -10, -10]))
