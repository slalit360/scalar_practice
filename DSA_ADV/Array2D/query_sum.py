"""
Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom, and columns are numbered from left to right.
Sum may be large, so return the answer mod 109 + 7.
"""


# brute force
from DSA_ADV.Array2D.prefix_sum import prefix_sum, prefix_sum2


def solve_naive(A, B, C, D, E):
    # TC : O(q * n * m)
    # SC : O(1)
    ans = []
    Q = len(B)
    for q in range(Q):
        summ = 0
        for i in range(B[q] - 1, D[q]):  # rows
            for j in range(C[q] - 1, E[q]):  # cols
                summ += A[i][j]
        ans.append(summ % (10 ** 9 + 7))
    return ans


# prefix sum of only rows
def solve_ps_row(A, B, C, D, E):
    # TC : O(n * m) + O(q * n)
    # SC : O(m * n)
    m = len(A)
    n = len(A[0])
    ps = [[0] * n for _ in range(m)]

    for i in range(m):
        ps[i][0] = A[i][0]
        for j in range(1, n):
            ps[i][j] = ps[i][j - 1] + A[i][j]

    qn = len(B)
    ans = []
    for q in range(qn):
        B[q] -= 1
        C[q] -= 1
        D[q] -= 1
        E[q] -= 1
        summ = 0
        for i in range(B[q], D[q] + 1):
            summ += ps[i][E[q]] - (ps[i][C[q] - 1] if C[q] > 0 else 0)
        ans.append(summ % (10 ** 9 + 7))
    return ans


# prefix sum of both rows and cols
def solve_ps(A, B, C, D, E):
    # TC : O(n * m) + O(q)
    # SC : O(m * n)
    ps = prefix_sum2(A)
    ans = []
    for q in range(len(B)):
        r1 = B[q] - 1
        c1 = C[q] - 1
        r2 = D[q] - 1
        c2 = E[q] - 1
        if r1 != 0 and c1 != 0:
            summ = ps[r2][c2] - ps[r1 - 1][c2] - ps[r2][c1 - 1] + ps[r1 - 1][c1 - 1]
        elif r1 == 0 and c1 != 0:
            summ = ps[r2][c2] - ps[r2][c1 - 1]
        elif r1 != 0 and c1 == 0:
            summ = ps[r2][c2] - ps[r1 - 1][c2]
        else:
            summ = ps[r2][c2]
        ans.append(summ % (10 ** 9 + 7))
    return ans


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = [1, 2]
    C = [1, 2]
    D = [2, 3]
    E = [2, 3]
    print(solve_ps(A, B, C, D, E))
