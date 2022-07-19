"""
Q1. Sum of all Submatrices
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.
"""

from DSA_ADV.Array2D.prefix_sum import prefix_sum


# Total # of sub-matrices : O(n^2 * m^2) of matrix size m x n

# 1. Brute force :
# consider all sub-matrices and find sum of each sub-matrix
# TC : O(n^3 * m^3)

# 2. prefix sum
# consider all sub-matrices and find sum with prefix sum
# TC : O(n^2 * m^2)
# SC : O(n * m)
# ToDo : verify /complete this
def solve_ps(A):
    m = len(A)
    n = len(A[0])
    ps = prefix_sum(A)
    summ = 0
    for ai in range(m):
        for aj in range(n):
            for bi in range(ai, m):
                for bj in range(n):
                    summ += (ps[bi][bj] - ps[ai - 1][bj] - ps[bi][aj - 1] + ps[ai - 1][aj - 1])
    return summ


# 3. contribution technique
# TC : O(m * n)
# SC : O(1)
def solve_contribution(A):
    m = len(A)
    n = len(A[0])
    summ = 0
    for i in range(m):
        for j in range(n):
            freq = (i + 1) * (n - i) * (j + 1) * (m - j)
            summ += freq * A[i][j]
    return summ


if __name__ == '__main__':
    A = [[1, 1],
         [1, 1]]
    print(solve_contribution(A))
