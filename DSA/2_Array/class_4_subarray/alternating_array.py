"""
Q3. Alternating Subarrays Easy
Problem Description
You are given an integer array A of length N comprising of 0's & 1's, and an integer B.

You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.

A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's.
For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.
"""


def solve(A, B):
    l = 2 * B + 1
    n = len(A)

    if B <= 0:
        return list(range(n))
    else:
        idx = []
        start = 0

        for i in range(1, n):
            if start > n - l:
                break
            if A[i] == A[i - 1]:
                start = i
            elif i - start + 1 == l:
                idx.append(start + (i - start + 1) // 2)
                start += 1
        return idx


if __name__ == '__main__':
    print(solve([1, 0, 1, 0, 1], 1))
    print(solve([0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1], 1))
    print(solve([0, 0, 0, 1, 1, 0, 1], 0))
