"""
Q4. Sub-array with 0 or K sum

Given an array of int A, find and return whether the given array contains a non-empty sub array with a sum equal to 0/K.

If the given array contains a sub-array with sum K return True, else return False.
"""


def longest_sub_array_sum_naive(A, K):
    # TC : O(n^3)
    # SC : O(1)
    n = len(A)
    s = 0
    e = 0
    max_l = 0
    for i in range(n):
        for j in range(i, n):
            tmp = sum(A[i:j + 1])
            if tmp == K:
                if j - i + 1 > max_l:
                    max_l = j - i + 1
                    s = i
                    e = j+1
                # print(i, j, j - i + 1, " -> ", A[i:j+1])
    if max_l == 0:
        return []

    return A[s:e]


def longest_sub_array_sum_prefix_sum(A, K):
    # with prefix sum
    # TC : O(N^2)
    # SC : O(N)
    n = len(A)
    ps = [A[0]]
    for i in range(1, n):
        ps.append(ps[i - 1] + A[i])

    s = 0
    e = 0
    max_l = 0
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                summ = ps[j]
            else:
                summ = ps[j] - ps[i - 1]
            if summ == K:
                if j - i + 1 > max_l:
                    max_l = j - i + 1
                    s = i
                    e = j + 1
                # print(i, j, j - i + 1, " -> ", A[i:j+1])
    if max_l == 0:
        return []
    return A[s:e]


def longest_sub_array_sum_carry_forward(A, K):
    # with carry forward sum
    # TC : O(N^2)
    # SC : O(1)
    n = len(A)
    s, e, max_l = 0, 0, 0
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += A[j]
            if summ == K:
                if j - i + 1 > max_l:
                    max_l = j - i + 1
                    s = i
                    e = j+1
                print(i, j, j - i + 1, " -> ", A[i:j+1])
    if max_l == 0:
        return []
    return A[s:e]


# this will be used just for longest subarray it might skip some of smaller subarrays to trace
def longest_zero_sum_sub_array_hashing(A):
    # hashing way :
    #  1. calc prefix sum
    #  2. check if any no repeats in ps and then sum will be Zero
    # TC : O(N)
    # SC : O(N)
    n = len(A)
    ps = [A[0]]
    for i in range(1, n):
        ps.append(ps[i - 1] + A[i])

    s = 0
    e = 0
    max_l = 0
    hashmap = dict()

    for i in range(n):
        if ps[i] == 0:
            j = 0
            print(j, i, i+1-j, " -> ", A[j:i+1])
            if i - j + 1 > max_l:
                max_l = i - j + 1
                s = 0
                e = i+1
        if ps[i] not in hashmap:
            hashmap[ps[i]] = i
        else:
            j = hashmap[ps[i]]
            if i - j + 1 > max_l:
                max_l = i - j + 1
                s = j+1
                e = i+1
            print(j+1, i, i-(j+1)+1, " -> ", A[j+1:i+1])
    if max_l == 0:
        return []

    return A[s:e]


# covers all sub array like carry forward os prefix sum approach
def longest_zero_sum_sub_array_hashmap_new(A):
    # hashing way :
    # TC : O(N)
    # SC : O(N)
    hashmap = dict()
    summ = 0
    n = len(A)
    max_l, s, e = 0, 0, 0
    for i in range(n):
        summ += A[i]

        if summ == 0:
            if max_l < i - 0 + 1:
                max_l = i - 0 + 1
                s = 0
                e = i + 1
            print(0, i, i-0+1, " -> ", A[0:i+1])

        al = []
        if summ in hashmap:
            al = hashmap[summ]
            for k in range(len(al)):
                j = al[k]
                if max_l < i - j + 1:
                    max_l = i - j + 1
                    s = j
                    e = i + 1
                print(j+1, i,  i-j, " -> ", A[j+1:i+1])
        al.append(i)
        hashmap[summ] = al

    return A[s:e]


if __name__ == '__main__':
    A = [0, 2, 3, -5, 1, -1, 1, 0] # + [4, 3, 2, -2, -3, 5, -3, 1, 2, 0]
    print(A, "\n")
    for K in [0]:  # , 1, 2, 3, 4, 5]:
        print(f"---- K : {K} ------")
        # print(longest_sub_array_sum_naive(A, K), "")
        # print(longest_sub_array_sum_prefix_sum(A, K), "")
        print(longest_sub_array_sum_carry_forward(A, K), "\n")

    # print("---- K : 0 ----")
    print(longest_zero_sum_sub_array_hashing(A), "\n")      # only checks for sum zero
    # print(longest_zero_sum_sub_array_hashing2(A), "\n")     # only checks for sum zero
    print(longest_zero_sum_sub_array_hashmap_new(A))        # only checks for sum zero
