"""
find no of pairs (0,1) pairs in the array (binary 1,0 only in array),
as their XOR value will be 1
1 ^ 0 = 1
"""


def cnt_pairs(A):
    # TC : O(n)
    cnt_zero = 0
    cnt_ones = 0
    for i in A:
        if i == 0:
            cnt_zero += 1
        else:
            cnt_ones += 1
    return cnt_ones * cnt_zero


"""
find sum of XOR of all the pairs of array A
A[i] ^ A[i] = 0
A[i] ^ A[j] = A[i] ^ A[j]
total n^2 pairs 
"""
import math


def sum_of_xor_pairs(A):
    # TC : O(n * log(max(A)) )
    ans = 0
    n = len(A)
    for i in range(int(math.log2(max(A)))):
        cnt = 0
        for e in A:
            if e & (1 << i) == 1:
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
    return 2 * ans


if __name__ == '__main__':
    print(cnt_pairs([0, 1, 1, 0, 0, 1, 0]))
    print(sum_of_xor_pairs([3, 5, 6, 8]))

