"""
HQ1 : K Occurrences

Groot has N trees lined up in front of him where the height of the i'th tree is denoted by H[i].
He wants to select some trees to replace his broken branches.
But he wants uniformity in his selection of trees.
So he picks only those trees whose heights have frequency K.
He then sums up the heights that occur K times. (He adds the height only once to the sum and not K times).
But the sum he ended up getting was huge so he prints it modulo 10^9+7.
In case no such cluster exists, Groot becomes sad and prints -1

Input:
N=5 ,K=2 ,A=[1 2 2 3 3]
Output: 5
Explanation:
There are 3 distinct numbers in the array which are 1,2,3.
Out of these, only 2 and 3 occur twice. Therefore the answer is sum of 2 and 3 which is 5.
"""


def getSum(n, k, A):
    # TC : O(n)
    # SC : O(n)
    hashmap = dict()

    for i in A:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    summ = 0
    flag = False
    for key, val in hashmap.items():
        if val == k:
            summ = (summ + key) % ((10 ** 9) + 7)
            flag = True

    if not flag:
        return -1
    else:
        return summ


if __name__ == '__main__':
    print(getSum(5, 2, [1, 2, 2, 3, 3]))
    print(getSum(3, 2, [1, 0, 0]))
    print(getSum(3, 2, [1, 0, -1]))
