def make_row_col_zero(A):
    """
    You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0.
    Specifically, make entire ith row and jth column zero.
    :param A:
    :return:
    """
    n = len(A)
    m = len(A[0])

    zr = dict()
    zc = dict()
    for i in range(0, n):
        for j in range(0, m):
            if A[i][j] == 0:
                zr[i] = 0
                zc[j] = 0
            else:
                zr[i] = zr[i] if i in zr else 1
                zc[j] = zc[j] if j in zc else 1

    for i in range(0, n):
        for j in range(0, m):
            if zr[i] == 0 or zc[j] == 0:
                A[i][j] = 0
    return A


if __name__ == '__main__':
    A = [
        [0, 1, 2],
        [3, 0, 4],
        [5, 6, 0]
    ]
    print(*A, sep="\n")
    make_row_col_zero(A)
    print(*A, sep="\n")