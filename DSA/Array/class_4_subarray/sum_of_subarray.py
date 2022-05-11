"""
Q2. Sum of All Subarrays

Problem Description
    You are given an integer array A of length N.
    You have to find the sum of all subarray sums of A.
    More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more
    elements from either end of the array.
    A subarray sum denotes the sum of all the elements of that subarray.

Sol : (n - i) * (i + 1) * A[i]
"""


def subarraySum(A):
    n = len(A)
    sumn = 0

    for i in range(n):
        freq = (n - i) * (i + 1)
        sumn = sumn + (A[i] * freq)

    return sumn