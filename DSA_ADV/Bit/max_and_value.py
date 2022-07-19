"""
given an array of n positive numbers,
find the max AND value of any pairs
"""

# BF : consider all pairs
# TC : O(n^2)
import math


def max_and(A):
    # TC : O(n * log(max))
    ans = 0
    for i in range(int(math.log2(max(A))) + 1, -1, -1):
        cnt = 0
        for j in A:
            if j & (1 << i):
                cnt += 1
        if cnt >= 2:
            ans += (1 << i)
            for k in range(len(A)):
                if A[k] & (1 << i):
                    A[k] = 0
    return ans


"""
find no of pairs with this max AND value
# find non zero elements Nc2
"""

"""
find max A[i] & A[j] & A[k] & A[l] where i != j != k != l
# use cnt >= 4 condition in above code
"""

if __name__ == '__main__':
    print(max_and([2, 3, 4, 5, 6]))


