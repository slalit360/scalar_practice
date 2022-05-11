# no of diag
"""
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.
"""


def print_diagonal(a, n, m):
    for j in range(m):
        x = 0
        y = j
        while x < n and y >= 0:
            print(a[x][y], end=", ")
            x += 1
            y -= 1
        print(" ")

    for j in range(1, n):
        x = j
        y = m - 1
        while x < n and y >= 0:
            print(a[x][y], end=", ")
            x += 1
            y -= 1
        print(" ")


def list_diagonal(A):
    n = len(A)
    out = []

    for i in range(n):
        x = 0
        y = i
        tmp = [0] * n
        k = 0
        while x < n and y >= 0:
            tmp[k] = A[x][y]
            x += 1
            y -= 1
            k += 1
        out.append(tmp)

    for i in range(1, n):
        x = i
        y = n - 1
        tmp = [0] * n
        k = 0
        while x < n and y >= 0:
            tmp[k] = A[x][y]
            x += 1
            y -= 1
            k += 1
        out.append(tmp)

    return


def main_diagonal_sum(A):
    """
    You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.

    Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

    :param A:
    :return:
    """
    m = len(A)
    summ = 0
    for i in range(m):
        summ += A[i][i]
    return summ


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(print_diagonal(A, 3, 3))
    print(list_diagonal(A))
    print(main_diagonal_sum(A))
