"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""


# brute force will be O(m * n)
# approach 1: use binary earch on each row or each col : O(m * log n)

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # TC : O(m+n)
    m = len(matrix)
    n = len(matrix[0])
    i = m - 1
    j = 0
    while i >= 0 and j < n:
        if matrix[i][j] == target:
            return True
        elif target < matrix[i][j]:
            i -= 1
        else:
            j += 1
    return False


def search(A, B):
    m = len(A)
    n = len(A[0])
    i = 0
    j = n - 1
    ans = -1
    while i < m and j >= 0:
        if A[i][j] == B:
            tmp = ((i + 1) * 1009) + (j + 1)
            if ans == -1:
                ans = tmp
            else:
                ans = min(ans, tmp)
            j -= 1
        elif B > A[i][j]:
            i += 1
        else:
            j -= 1
    return ans


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
              ]
    target = 20
    print(searchMatrix(matrix, target=14))
    print(searchMatrix(matrix, target=45))

    A = [[1, 2, 2],
         [4, 5, 6],
         [7, 8, 9]]
    B = 2
    print(search(A, B))
