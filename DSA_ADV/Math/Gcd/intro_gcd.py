def gcd_naive(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def gcd_minus(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd_minus(b, a - b)
    return gcd_minus(a, b - a)


def gcd_mod(a, b):
    # assume a >= b
    if b == 0:
        return a
    else:
        return gcd_mod(b, a % b)


if __name__ == '__main__':
    a = 10
    b = 8
    print(gcd_naive(a, b))
    print(gcd_minus(a, b))
    print(gcd_mod(a, b))


import math


class Solution:
    def gcd(self, a, b):
        while a % b != 0:
            a, b = b, a % b
        return b

    def solve(self, A):
        n = len(A)
        if n < 2:
            return A

        A.sort(reverse=True)

        if n < 5:
            return A[:2]

        ans = []
        m = int(math.sqrt(n))

        freq = {}
        for el in A:
            freq[el] = freq.get(el, 0) + 1

        ans.append(A[0])
        ans.append(A[1])

        freq[self.gcd(A[0], A[1])] -= 2

        i = 2
        while i < n:
            if freq[A[i]] > 0:
                ans.append(A[i])
            if len(ans) == m:
                return ans
            for k in range(0, i+1):
                freq[self.gcd(A[k], A[i])] -= 2
            i += 1
        return ans
