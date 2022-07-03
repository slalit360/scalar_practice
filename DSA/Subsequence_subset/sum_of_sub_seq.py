def sum_of_all_sub_seq_naive(A):
    # find sum of all sub sequences
    # TC : O(n * 2^n)
    ans = 0
    n = len(A)
    for i in range(1 << n):
        summ = 0
        for j in range(n):
            if i & (1 << j):
                summ += A[j]
        ans += summ
    return ans


def sum_of_all_sub_seq(A):
    # find sum of all sub sequences
    # tech : contribution technique
    # obs : no of subset in which any A[i] is present : 2^(n-1)
    # TC : O(n)
    n = len(A)
    return sum(A) * (1 << n - 1)  # sum(A) * 2**(n-1)


if __name__ == '__main__':
    print(sum_of_all_sub_seq([3, 1, 4]))
