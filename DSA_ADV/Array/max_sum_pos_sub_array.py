import math


def max_sum_pos_subarray(A):
    # TC : O(n)
    n = len(A)
    maxx = -math.inf
    l = 0
    s, e = -1, -1

    for i in range(n):
        if A[i] >= 0:

            for j in range(i, n):
                if A[j] >= 0:

                    tmp = sum(A[i:j + 1])
                    if tmp > maxx:
                        maxx = tmp
                        s = i
                        e = j
                    if tmp == maxx and j - i + 1 >= l:
                        maxx = tmp
                        s = i
                        e = j
                        l = e - s + 1
                else:
                    break
    if s == -1 and e == -1:
        return []
    return A[s:e + 1]


if __name__ == '__main__':
    print(max_sum_pos_subarray([1, 2, 5, -7, 2, 5]))
    print(max_sum_pos_subarray([0, 0, -1, 0]))
    print(max_sum_pos_subarray([756898537, -1973594324, -2038664370, -184803526, 1424268980]))
