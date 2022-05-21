def pick_from_both_end_n_space(A, B):
    n = len(A)

    ps = [0] * n
    ps[0] = A[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + A[i]

    max_sum = 0
    l = B - 1
    r = n
    while l >= 0:
        summ = ps[l] + (ps[n - 1] - ps[r - 1])
        max_sum = max(max_sum, summ)
        l -= 1
        r -= 1
    max_sum = max(max_sum, ps[n - 1] - ps[n - B - 1])
    return max_sum


def pick_from_both_end(A, B):
    n = len(A)
    curr_point = sum(A[:B])
    max_point = curr_point
    j = n - 1
    for i in range(B - 1, -1, -1):
        curr_point = curr_point + A[j] - A[i]
        max_point = max(curr_point, max_point)
        j -= 1
    return max_point


print(pick_from_both_end_n_space(A=[5, -2, 3, 1, 2], B=3))
print(pick_from_both_end(A=[5, -2, 3, 1, 2], B=3))
print(pick_from_both_end_n_space(A=[1, 2], B=1))
print(pick_from_both_end(A=[1, 2], B=1))
