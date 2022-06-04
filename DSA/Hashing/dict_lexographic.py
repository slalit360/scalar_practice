"""
Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language,
and the order of the alphabet denoted by string B of size 26,
return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.
"""

from functools import cmp_to_key


def solve(A, B):
    hashmap = dict()
    for i, k in enumerate(B):
        hashmap[k] = i

    def compare(a, b):
        na = len(a)
        nb = len(b)
        i = 0
        while i < min(na, nb):
            if hashmap[a[i]] > hashmap[b[i]]:
                return 1
            elif hashmap[a[i]] < hashmap[b[i]]:
                return -1
            else:
                i += 1

        if na > nb:
            return 1
        else:
            return -1

    sA = sorted(A, key=cmp_to_key(compare))
    for i in range(len(A)):
        if sA[i] != A[i]:
            return 0

    return 1


if __name__ == '__main__':
    A = ["hello", "scaler", "interviewbit"]
    # B = "abcdefghijklmnopqrstuvwxyz"
    B = "adhbcfegskjlponmirqtxwuvzy"
    print(solve(A, B))
    A = ["fine", "none", "no"]
    B = "qwertyuiopasdfghjklzxcvbnm"
    print(solve(A, B))
