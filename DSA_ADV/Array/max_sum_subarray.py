"""
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
"""
import math


def maxSubArray(A):
    # TC : O(n^2)
    import math
    n = len(A)
    ans = -math.inf
    for i in range(n):
        tmp_sum = 0
        for j in range(i, n):
            tmp_sum += A[j]
            ans = max(ans, tmp_sum)
    return ans


def maxSubArray_best(A):
    # TC : O(n)
    # kadane's algorithm
    n = len(A)
    curr_sum = A[0]
    max_sum = A[0]
    for i in range(1, n):
        curr_sum = max(curr_sum + A[i], A[i])  # += A[i]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


def maxSubArray_best(A):
    # TC : O(n)
    # kadane's algorithm
    n = len(A)
    curr_sum = 0  # A[0]
    max_sum = -math.inf  # A[0]
    # curr_arr = [A[0]]
    # final_arr = []
    s = 0
    e = 0
    start = 0
    end = 0

    for i in range(n):
        if curr_sum + A[i] > A[i]:
            curr_sum += A[i]
            # curr_arr.append(A[i])
            e += 1
        else:
            curr_sum = A[i]
            # curr_arr = [A[i]]
            s = i

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = s
            end = e
            # final_arr = curr_arr[:]

        if curr_sum < 0:
            curr_sum = 0

    # print("final_arr : ", final_arr)
    print(f"start : {start} , end : {start + end}")
    print(f"max_sum : {max_sum}")
    return " "


if __name__ == '__main__':
    print(maxSubArray_best([-4, -2, -3, -1, -5]))
    print(maxSubArray_best([4, 2, 3, 1, 5]))
    print(maxSubArray_best([-4, -2, 3, 2, -5]))
