def generate_spiral_matrix(A):
    """
    Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

    :param A:
    :return:
    """
    i = 0
    j = 0
    num = 1
    n = A

    if n == 1:
        return [[1]]

    M = [[0] * A for i in range(A)]

    while n > 1:

        for k in range(1, n):
            M[i][j] = num
            num += 1
            j += 1

        for k in range(1, n):
            M[i][j] = num
            i += 1
            num += 1

        for k in range(1, n):
            M[i][j] = num
            j -= 1
            num += 1

        for k in range(1, n):
            M[i][j] = num
            i -= 1
            num += 1

        i += 1
        j += 1
        n -= 2

    if n % 2 == 1:
        M[i][j] = num

    return M


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(*a, sep="\n")
    print(" ")
    print(*generate_spiral_matrix(4), sep="\n")
