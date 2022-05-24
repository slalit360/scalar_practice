"""
Given an array A and an integer B.
A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.
"""


def check_sum(A, B):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] + A[j] == B:
                return 1
    return 0


if __name__ == '__main__':
    print(check_sum([3, -2, 1, 4, 3, 6, 8], 10))