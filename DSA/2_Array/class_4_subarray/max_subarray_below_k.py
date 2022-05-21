"""
Q4. Maximum Subarray Easy

Problem Description
    You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum
    of contiguous elements is maximum.
    But the sum must not exceed B.

"""
import math


def maxSubarray(N, S, Arr):

    ps = [Arr[0]]
    for i in range(1, N):
        ps.append(ps[i-1] + Arr[i])

    maxn = -math.inf

    for i in range(N):
        for j in range(i, N):
            if i == 0 or j == 0:
                tmp = ps[j]
            else:
                tmp = ps[j] - ps[i-1]
            if maxn < tmp <= S:
                maxn = tmp

    return maxn

"""
H1 : Counting Subarray
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.
"""


def solve(A, B):
    N = len(A)
    ps = [A[0]]
    for i in range(1, N):
        ps.append(ps[i - 1] + A[i])

    count = 0

    for i in range(N):
        for j in range(i, N):
            if i == 0 or j == 0:
                tmp = ps[j]
            else:
                tmp = ps[j] - ps[i - 1]
            if tmp < B:
                count += 1

    return count


"""
Q2. Good Subarrays 

Problem Description
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.
"""


def solve2(A, B):
    N = len(A)
    ps = [A[0]]
    for i in range(1, N):
        ps.append(ps[i - 1] + A[i])

    count = 0

    for i in range(N):
        for j in range(i, N):
            if i == 0 or j == 0:
                tmp = ps[j]
            else:
                tmp = ps[j] - ps[i - 1]

            l = (j - i + 1)

            if (l % 2 == 0 and tmp < B) or (l % 2 == 1 and tmp > B):
                count += 1

    return count