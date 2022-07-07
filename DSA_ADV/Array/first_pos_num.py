"""
Q5. First Missing Integer

Problem Description
Given an unsorted integer array, A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.
"""


def firstMissingPositive(A):
    # TC : O(n)
    # SC : O(1)
    h = set(A)
    n = len(A)
    for i in range(1, n + 2):
        if i not in h:
            return i


if __name__ == '__main__':
    print(firstMissingPositive([-1, 3, 0, 2, 5, -9]))
    print(firstMissingPositive([-1, 4, 1, 2, 5, -9]))
    print(firstMissingPositive([-1, 5, 0, 1, 2, 3]))
