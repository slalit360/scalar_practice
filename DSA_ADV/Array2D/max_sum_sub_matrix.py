"""
Max sum Sub-matrix
"""
import math

from DSA_ADV.Array2D.prefix_sum import prefix_sum, prefix_sum2


# 1. Naive Approach:
# The simplest approach is to generate all possible submatrices from the given matrix and calculate their sum
# Time Complexity: O(N^6)
# Auxiliary Space: O(1)
def kadanes(A):
    curr_sum = 0
    max_sum = -math.inf
    for i in range(len(A)):
        curr_sum += A[i]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


# 2. Efficient Approach using row prefix sum + Kadane’s Algorithm:
# Time Complexity: O(N^3)
# Auxiliary Space: O(N)
def max_sum_sub_matrix(A):
    m = len(A)
    n = len(A[0])

    ps = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ps[i][j] = A[i][j] + (ps[i][j - 1] if j > 0 else 0)

    max_sum = -math.inf
    for i in range(n):
        for j in range(i, n):
            arr = []
            for k in range(m):
                el = ps[k][j] - (ps[k][i - 1] if i > 0 else 0)
                arr.append(el)
            max_sum = max(max_sum, kadanes(arr))
    return max_sum


"""
Q3. Maximum Sum Square SubMatrix of Size B

Given a 2D integer matrix A of size N x N, find a B x B sub-matrix where B<= N and B>= 1,
such that the sum of all the elements in the sub-matrix is maximum.
"""


# 2. Efficient Approach using prefix sum:
# Time Complexity: O(N^2)
# Auxiliary Space: O(N)
def max_sum_sub_matrix_B(A, B):
    m = len(A)
    n = len(A[0])
    ps = prefix_sum2(A, m, n)
    max_sum = -math.inf

    for i in range(m-B+1):
        for j in range(n-B+1):
            r = i + B -1
            c = j + B - 1
            if i == 0 and j == 0:
                curr_sum = ps[r][c]
            elif i == 0:
                curr_sum = ps[r][c] - ps[r][j-1]
            elif j == 0:
                curr_sum = ps[r][c] - ps[i-1][c]
            else:
                curr_sum = ps[r][c] - ps[i - 1][c] - ps[r][j - 1] + ps[i - 1][j - 1]
            max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == '__main__':
    A = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
    ]
    B = 5  # 48
    print(max_sum_sub_matrix(A))
    print(max_sum_sub_matrix_B(A, B))

