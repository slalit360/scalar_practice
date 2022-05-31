import math


def consecutive_1s_count(A):
    """
    Given a binary string A. It is allowed to do at most one swap between any 0 and 1.
    Find and return the length of the longest consecutive 1’s that can be achieved.
    # TC seems like O(n^2) but it is O(n) as every element is accessed max three times.
    """
    n = len(A)
    ans = 0

    count_of_1 = 0
    for i in range(n):
        if A[i] == '1':
            count_of_1 += 1
    flag = False
    for i in range(n):
        # print(A[i])
        if A[i] == '0':
            if not flag:
                l = 0
                for j in range(i - 1, -1, -1):
                    if A[j] == '1':
                        l += 1
                    else:
                        break
            else:
                l = r
            r = 0
            for j in range(i + 1, n):
                if A[j] == '1':
                    r += 1
                else:
                    break
            if l + r < count_of_1:
                tmp = l + r + 1
            else:
                tmp = l + r
            ans = max(ans, tmp)

    if ans == 0:
        return n
    else:
        return ans


def get_min_cost(A, B):
    """
    You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the
    cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)),
    and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.

    The cost of these trees is Bp + Bq + Br.

    You are to choose 3 trees such that their total cost is minimum. Return that cost.

    If it is not possible to choose 3 such trees return -1.
    :param A:
    :param B:
    :return:
    """
    n = len(A)
    min_cost = math.inf
    for j in range(1, n - 1):

        min_bp = math.inf
        for i in range(j):
            if A[i] < A[j]:
                min_bp = min(min_bp, B[i])

        min_br = math.inf
        for k in range(j + 1, n):
            if A[k] > A[j]:
                min_br = min(min_br, B[k])

        if min_bp != math.inf and min_br != math.inf:
            min_cost = min(min_cost, min_bp + B[j] + min_br)

    if min_cost != math.inf:
        return min_cost

    return -1


def print_diamond(n):
    for i in range(n):
        t: str = '*' * (n - i)
        s: str = ' ' * (i * 2)
        print(t + s + t)

    for i in range(n - 1, -1, -1):
        t: str = '*' * (n - i)
        s: str = ' ' * (i * 2)
        print(t + s + t)


def smallestNumber(num: int) -> int:
    num = list(str(num))
    num.sort()
    tmp = None
    for i, n in enumerate(num):
        if n != '0':
            tmp = num.pop(i)
            break

    return str(tmp) + ''.join(num)


def specialXor(N, Q, a, query):
    ps = [0] * N
    ps[0] = a[0]
    for i in range(1, N):
        ps[i] = a[i] ^ ps[i - 1]

    ps1 = [0] * N
    ps1[N - 1] = a[N - 1]
    for i in range(N - 2, -1, -1):
        ps1[i] = a[i] ^ ps1[i + 1]

    res = []
    for i in range(Q):
        l = query[i][0]  # - 1
        r = query[i][1]  # - 1
        if l == 1:
            val = ps1[r]
        else:
            val = ps[l - 2] ^ ps1[r]
        res.append(val)
    return res


if __name__ == '__main__':
    print(smallestNumber(1234))
    A = "111011101"
    print(consecutive_1s_count(A))
    print_diamond(n=4)