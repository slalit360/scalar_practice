"""
P : Common elements

Given two integer arrays, A and B of size N and M, respectively.
Your task is to find all the common elements in both the array.

NOTE:

Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.
"""


def common_with_dup(A, B):
    b = dict()
    for i in B:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    common = []
    for i in A:
        if i in b and b[i] > 0:
            common.append(i)
            b[i] -= 1
    return common


if __name__ == '__main__':
    print(common_with_dup(A=[1, 2, 2, 1], B=[2, 3, 1, 2]))
