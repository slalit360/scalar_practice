"""
Given an integer array A of size N.
Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.

A sequence of numbers is called an AP if the difference between any two consecutive elements is the same.
"""


def check_if_AP(A):
    # O(n log n)
    A.sort()
    n = len(A)
    for i in range(1, n - 1):
        if A[i + 1] - A[i] != A[i] - A[i - 1]:
            return 0
    return 1


def check_if_AP2(A):
    # O(n)
    n = len(A)

    min1 = A[0]
    min0 = A[0]
    for i in A:
        if i < min0:
            min0 = min1
            min1 = i

    s = set(A)
    d = abs(min1 - min0)
    for i in range(n):
        if min1 + (i * d) not in s:
            return 0
    return 1


if __name__ == '__main__':
    print(check_if_AP([5, 4, 3, 2, 1, 0, -1]))
    print(check_if_AP2([5, 4, 3, 2, 1, 0, -1]))
