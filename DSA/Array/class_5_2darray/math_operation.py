def matrix_multiplication(A, B):
    m = len(A)
    n = len(A[0])

    n = len(B)
    p = len(B[0])

    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += (A[i][k] * B[k][j])

    return C


def column_sum(A):
    n = len(A)
    m = len(A[0])
    sum_amt = [0] * m

    for j in range(m):
        for i in range(n):
            sum_amt[j] += A[i][j]

    return sum_amt


def mat_sub(A, B):
    m = len(A)
    n = len(A[0])

    for i in range(m):
        for j in range(n):
            A[i][j] -= B[i][j]

    return A


def mat_add(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]

    return A
