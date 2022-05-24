from time_utility import timeit


def get_sum(A, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += A[i]
    return sum


def get_sum_prefix(A, start, end):
    sum_arr = [0] * len(A)
    sum_arr[0] = A[0]
    for i in range(1, len(A)):
        sum_arr[i] = sum_arr[i - 1] + A[i]
    # print(sum_arr)
    if start < 1:
        return sum_arr[end]
    else:
        return sum_arr[end] - sum_arr[start - 1]


A = list(range(1, 10 ** 5))
n = len(A)
q = 10 ** 5


@timeit
def approach1(A, n, q):
    for _ in range(q):
        get_sum(A, 0, n - 1)


@timeit
def approach2(A, n, q):
    for _ in range(q):
        get_sum_prefix(A, 0, n - 1)


# approach2(A, n, q)
# approach1(A, n, q)


"""
ou are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
"""


def rangeSum(A, B):
    n = len(A)
    ps = [0] * n

    ps[0] = A[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + A[i]
    # print(ps)
    op = []
    for start, end in B:
        start -= 1
        end -= 1
        if start < 1:
            res = ps[end]
        else:
            res = ps[end] - ps[start - 1]
        op.append(res)

    return op


if __name__ == '__main__':
    print(rangeSum(A=[1, 2, 3, 4, 5], B=[[1, 4], [2, 3]]))
