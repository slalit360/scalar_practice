def longSubarrWthSumDivByK(Arr, N, K):
    # prefix sum
    ps = [Arr[0]]
    for i in range(1, N):
        ps.append(ps[i - 1] + Arr[i])
    # print(ps)

    max_length = max([i + 1 for i in range(N) if ps[i] % K == 0])

    # print(max_length)
    start = 1
    end = 1
    while start < N and end < N:
        tmp = ps[end] - ps[start - 1]
        if tmp % K == 0:
            max_length = max(max_length, end - start + 1)
        end += 1
        if end == N - 1:
            start += 1
            end = start

    return max_length


def log_sub_array_sum_by_k_n2(Arr, N, K):
    max_length = 0

    ps = [Arr[0]]
    for i in range(1, N):
        ps.append(ps[i - 1] + Arr[i])

    for i in range(N):
        if i == 0:
            for j in range(N):
                if ps[j] % K == 0:
                    max_length = max(max_length, j + 1)
        else:
            for j in range(i, N):
                if (ps[j] - ps[i - 1]) % K == 0:
                    max_length = max(max_length, j - i + 1)

    return max_length


def log_sub_array_sum_by_k(Arr, N, K):
    max_length = 0

    ps = [Arr[0]]
    for i in range(1, N):
        ps.append(ps[i - 1] + Arr[i])

    mod_arr = [0] * N
    for i in range(N):
        mod_arr[i] = ps[i] % K

    print(ps)
    print(mod_arr)

    for i in range(N):
        if i == 0:
            for j in range(N):
                if ps[j] % K == 0:
                    max_length = max(max_length, j + 1)
        else:
            for j in range(i, N):
                if (ps[j] - ps[i - 1]) % K == 0:
                    max_length = max(max_length, j - i + 1)

    return max_length


if __name__ == '__main__':
    A = [2, 7, 6, 1, 4, 5]
    A1 = [-2, 2, -5, 12, -11, -1, 7]
    print(log_sub_array_sum_by_k(A, len(A), 3))
    print(log_sub_array_sum_by_k(A1, len(A1), 3))
    print(log_sub_array_sum_by_k([7, 8, 10], 3, 16))
