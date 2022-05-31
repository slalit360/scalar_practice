"""
Q2. Sum of All Sub-arrays

Problem Description
    You are given an integer array A of length N.
    You have to find the sum of all sub-array sums of A.
    More formally, a sub-array is defined as a contiguous part of an array which we can obtain by deleting zero or more
    elements from either end of the array.
    A sub-array sum denotes the sum of all the elements of that sub-array.

Sol : (n - i) * (i + 1) * A[i]
"""


def sum_of_all_sub_array(A):
    # TC : O(N)
    n = len(A)
    sumn = 0

    for i in range(n):
        freq = (n - i) * (i + 1)
        sumn = sumn + (A[i] * freq)

    return sumn


if __name__ == '__main__':
    print(sum_of_all_sub_array([1, 2, 3, 4, 5]))