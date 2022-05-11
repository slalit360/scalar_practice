def rotate_mat(A):
    """
    You are given a n x n 2D matrix A representing an image.

    Rotate the image by 90 degrees (clockwise).

    You need to do this in place.
    :param A:
    :return:
    """
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    # print(*A)
    for i in range(n):
        A[i] = A[i][::-1]


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(*a, sep="\n")
    print(" ")
    print(rotate_mat(a))
    print(*a, sep="\n")