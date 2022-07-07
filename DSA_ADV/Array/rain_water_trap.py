"""
Q2. Rain Water Trapped

Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""


def trap(A):
    # TC : O(n)
    # SC : O(n)
    ans = 0
    n = len(A)

    left_max = [0] * n
    left_max[0] = A[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], A[i])

    right_max = [0] * n
    right_max[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], A[i])

    for i in range(n):
        tmp = min(left_max[i], right_max[i]) - A[i]
        if tmp > 0:
            ans += tmp

    return ans


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap([4, 2, 0, 3, 2, 5]))
