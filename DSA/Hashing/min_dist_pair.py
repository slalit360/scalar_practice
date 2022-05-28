"""
Q5.
Shaggy has an array A consisting of N elements.
We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.

Shaggy wants you to find a special pair such that the distance between that pair is minimum.
Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.
"""
import math


def min_dist_of_dup_naive(A):
    # TC : O(n^2)
    # SC : O(1)
    mins = math.inf
    n = len(A)

    for i in range(n):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                mins = min(mins, abs(j - i))

    if mins == math.inf:
        return -1
    else:
        return mins


def min_dist_of_dup_best(A):
    # TC: O(n)
    # SC : O(n)
    mins = math.inf
    n = len(A)
    d = dict()

    for i in range(n):
        if A[i] not in d:
            d[A[i]] = i
        else:
            mins = min(mins, i - d[A[i]])

    if mins == math.inf:
        return -1
    else:
        return mins


if __name__ == '__main__':
    print(min_dist_of_dup_naive([7, 1, 3, 4, 1, 7]))
    print(min_dist_of_dup_best([7, 1, 3, 4, 1, 7]))

    print(min_dist_of_dup_naive([1, 1]))
    print(min_dist_of_dup_best([1, 1]))
