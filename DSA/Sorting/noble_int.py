"""
Given an integer array A,
find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

A = [3, 2, 1, 3]
1
For integer 2, there are 2 greater elements in the array..

A = [1, 1, 3, 3]
-1
There exist no integer satisfying the required conditions.
"""


def is_noble_no(A):
    # O(n log n)
    A.sort()
    n = len(A)
    for i in range(n - 1):
        if A[i] == n - i - 1 and A[i] != A[i + 1]:
            return 1
    if A[n - 1] == 0:
        return 1
    return -1


if __name__ == '__main__':
    print(is_noble_no([1, 3, 5, 4, 2, 9]))
    print(is_noble_no([1, 4, 4, 4, 8, 9]))
