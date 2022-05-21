def print_transpose(A, n, m):
    # works in case of non square matrix as well with extra space
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    # return zip(*A)


def print_transpose_1(A):
    # works only for square matrix : here swap is in place
    m = len(A)
    for i in range(m):
        for j in range(i + 1, m):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    return A


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(*print_transpose(A, 3, 3), sep="\n")
    print()
    print(*print_transpose_1(A), sep="\n")