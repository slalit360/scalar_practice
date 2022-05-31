"""
Q4. Sub-array with 0 or K sum

Given an array of int A, find and return whether the given array contains a non-empty sub array with a sum equal to 0/K.

If the given array contains a sub-array with sum K return True, else return False.
"""


def check_sub_array_sum_naive(A, K):
    # TC : O(n^3)
    # SC : O(1)
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            tmp = sum(A[i:j + 1])
            if tmp == K:
                # print(i, j, j - i + 1)
                return True
    return False


def check_sub_array_sum_prefix_sum(A, K):
    # with prefix sum
    # TC : O(N^2)
    # SC : O(N)
    n = len(A)
    ps = [A[0]]
    for i in range(1, n):
        ps.append(ps[i - 1] + A[i])

    for i in range(n):
        for j in range(i, n):
            if i == 0:
                tmp = ps[j]
            else:
                tmp = ps[j] - ps[i - 1]
            if tmp == K:
                # print(i, j, j - i + 1)
                return True
    return False


def check_sub_array_sum_carry_forward(A, K):
    # with carry forward sum
    # TC : O(N^2)
    # SC : O(1)
    n = len(A)

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += A[j]
            if summ == K:
                # print(i, j, j - i + 1)
                return True
    return False


def check_zero_sum_sub_array_hashing(A, K=0):
    # hashing way :
    #  1. calc prefix sum
    #  2. check if any no repeats in ps and then sum will be Zero
    # TC : O(N)
    # SC : O(N)
    n = len(A)
    ps = [A[0]]
    for i in range(1, n):
        ps.append(ps[i - 1] + A[i])

    hashset = set()
    for i in ps:
        if i == K:
            return True
        if i - K in hashset:
            return True
        else:
            hashset.add(i)

    return False


def check_zero_sum_sub_array_hashing2(A):
    # TC : O(N)
    # SC : O(1)
    d = set()
    curr_sum = 0
    for x in A:
        curr_sum += x
        if curr_sum == 0 or x == 0 or curr_sum in d:
            return True
        else:
            d.add(curr_sum)
    return False


if __name__ == '__main__':
    A = [1, -3, 1, 2, -4, 6, 2, -4, 1, -5, 7]
    for K in [10, 11, 12, 3, 4, 5]:
        print(f"---- K : {K} ------")
        print(check_sub_array_sum_naive(A, K))
        print(check_sub_array_sum_prefix_sum(A, K))
        print(check_sub_array_sum_carry_forward(A, K))
        print(check_zero_sum_sub_array_hashing(A, K))
    # print("---- K : 0 ----")

    # print(check_zero_sum_sub_array_hashing2(A), "\n")  # only checks for sum zero
