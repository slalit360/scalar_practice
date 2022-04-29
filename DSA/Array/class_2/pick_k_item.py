
def pick_from_both_end(A, B):
    n = len(A)
    curr_point = sum(A[:B])
    max_point = curr_point
    j = n - 1
    for i in range(B-1, -1, -1):
        curr_point = curr_point + A[j] - A[i]
        max_point = max(curr_point, max_point)
        j -= 1
    return max_point


print(pick_from_both_end(A=[5, -2, 3, 1, 2], B=3))

print(pick_from_both_end(A=[1, 2], B=1))
