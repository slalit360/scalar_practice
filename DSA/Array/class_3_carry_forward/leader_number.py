"""
Given an integer array A containing N distinct integers, you have to find all the leaders in array A.

An element is a leader if it is strictly greater than all the elements to its right side.

NOTE:The rightmost element is always a leader.
"""


def get_leaders(A):
    # find right max array
    n = len(A)
    rm = [0] * n
    rm[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        rm[i] = max(rm[i + 1], A[i])

    leaders = []
    for i in range(n):
        if rm[i] == A[i]:
            leaders.append(A[i])

    return leaders


if __name__ == '__main__':
    A = [16, 17, 4, 3, 5, 2]
    A1 = [1, 2]
    # print(*A)
    print(get_leaders(A))
    print(get_leaders(A1))
