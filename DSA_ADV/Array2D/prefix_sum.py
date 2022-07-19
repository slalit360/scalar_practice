def prefix_sum(A, m=None, n=None):
    # TC : O(m*n)
    if m is None and n is None:
        m = len(A)
        n = len(A[0])
    ps = [[0] * n for _ in range(m)]

    # first row prefix sum
    for i in range(m):
        sums = 0
        for j in range(n):
            sums += A[i][j]
            ps[i][j] = sums

    # then col prefix sum
    for i in range(m):
        sums = 0
        for j in range(n):
            sums += ps[j][i]
            ps[j][i] = sums

    print(*ps, sep="\n")
    return ps


def prefix_sum2(A, m=None, n=None):
    if m is None and n is None:
        m = len(A)
        n = len(A[0])
    ps = [[0] * n for _ in range(m)]

    ps[0][0] = A[0][0]

    # filling first row
    for i in range(1, m):
        ps[0][i] = ps[0][i - 1] + A[0][i]

    # filling first col
    for i in range(1, n):
        ps[i][0] = ps[i - 1][0] + A[i][0]

    # updating remaining cells
    for i in range(1, m):
        for j in range(1, n):
            ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + A[i][j]
    print(*ps, sep="\n")

    return ps


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    prefix_sum(A)
    print(" ")
    A = [
        [-1]
    ]
    prefix_sum2(A)
