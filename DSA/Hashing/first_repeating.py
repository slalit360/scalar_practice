"""
P : First Repeating element
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.

If there is no repeating element, return -1.
"""


def first_repeating_naive(A):
    dup = set()
    tmp = set()
    for i in range(len(A)):
        if A[i] in tmp:
            dup.add(A[i])
        else:
            tmp.add(A[i])
    for i in A:
        if i in dup:
            return i
    return -1


def first_repeating(A):
    n = len(A)
    ans = -1
    ump = set()
    for i in range(n - 1, -1, -1):
        if A[i] in ump:
            ans = A[i]
        else:
            ump.add(A[i])
    return ans


if __name__ == '__main__':
    print(first_repeating_naive([10, 5, 3, 4, 3, 5, 6]))
    print(first_repeating([10, 5, 3, 4, 3, 5, 6]))
