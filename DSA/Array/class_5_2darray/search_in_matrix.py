"""
Q : search in sorted array
Given 2D Array of size m x n and Integer B,
Note : rows and columns both are increasingly sorted.
find and return position of element B if found else return -1
"""


# 1. Brute force approach will take : O(m*n)
# 2. Apply Binary search for every row : O(m * log n)

def search_index(A, B):
    # TC : O(m+n)

    m = len(A)
    n = len(A[0])

    if B < A[0][0] or B > A[m-1][n-1]:
        return -1

    i = 0
    j = n - 1

    while i < m and j >= 0:

        if A[i][j] == B:
            return i, j

        elif A[i][j] > B:
            j -= 1
        else:
            i += 1

    return -1


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(search_index(A, 7))
