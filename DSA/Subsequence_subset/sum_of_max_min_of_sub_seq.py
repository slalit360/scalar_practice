def sum_of_max_sub_seq_naive(A):
    # consider all subsequences, find max from each and sum it up
    # TC : (n * 2^n)
    pass


def sum_of_max_sub_seq(A):
    # return sum of all max from each subsequence of array
    # tech : contribution technique
    # obs : a[i] is max in 2^i subsequences
    # TC : O(n log n)
    n = len(A)
    A.sort()
    ans = 0
    for i in range(n):
        ans += (A[i] * (1 << i))
    return ans


def sum_of_min_sub_seq_naive(A):
    # consider all subsequences, find min from each and sum it up
    # TC : (n * 2^n)
    pass


def sum_of_min_sub_seq(A):
    # return sum of all min from each subsequence of array
    # tech : contribution technique
    # obs : a[i] is max in 2^i subsequences
    # TC : O(n log n)
    n = len(A)
    A.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += (A[i] * (1 << i))
    return ans


def sum_of_diff_max_min_sub_seq(A):
    # return sum of diff of max, min from each subsequence of array
    # tech : contribution technique
    # obs : a[i] is max in 2^i subsequences
    # TC : O(n log n)
    n = len(A)
    A.sort()
    mod = 1000000007  # 10^9 + 7
    max_sum = 0
    min_sum = 0
    for i in range(n):
        max_sum += A[i] * ((1 << i) % mod)
        min_sum += A[n-i-1] * ((1 << i) % mod)
    return (max_sum - min_sum) % mod


if __name__ == '__main__':
    print(sum_of_max_sub_seq([3, 5, 7, 8, 9]))
    print(sum_of_min_sub_seq([3, 5, 7, 8, 9]))
    print(sum_of_diff_max_min_sub_seq([3, 5, 7, 8, 9]))
