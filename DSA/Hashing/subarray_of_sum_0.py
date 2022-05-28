"""
Q4. Sub-array with 0 sum

Given an array of int A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

If the given array contains a sub-array with sum zero return 1, else return 0.
"""


def check_sum_is_zero_naive(A):
    # O(n^2)
    n = len(A)

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += A[j]
            if summ == 0:
                return 1

    else:
        return 0


def check_sum_is_zero_best(A):
    # O(n)
    d = set()
    curr_sum = 0
    for x in A:
        curr_sum += x
        if curr_sum == 0 or x == 0 or curr_sum in d:
            return 1
        else:
            d.add(curr_sum)
    return 0


if __name__ == '__main__':
    print(check_sum_is_zero_naive([5, -1, 1, 2]))
    print(check_sum_is_zero_best([5, -1, 1, 2]))
    print(check_sum_is_zero_naive([1, 2, 3]))
    print(check_sum_is_zero_best([1, 2, 3]))
