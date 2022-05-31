def get_max_size_pos_sub_array(A):
    """
    Given an array of integers A, of size N.

    Return the maximum size sub-array of A having only non-negative elements. If there are more than one such sub-array,
    return the one having the smallest starting index in A.
    NOTE: It is guaranteed that an answer always exists.

    :param A:
    :return:
    """
    N = len(A)
    maximum = 0
    start_index = 0
    count = 0
    for i in range(N):
        if A[i] > 0:
            if count == 0:
                k = i  # note the starting point of each positive subarray
            count += 1
        if A[i] < 0 or (i == N - 1):
            if count > maximum:
                start_index = k  # this will be the starting point of the answer
                maximum = count
            count = 0
    return A[start_index:start_index + maximum]


if __name__ == '__main__':
    print(get_max_size_pos_sub_array([1, 2, 3, -1, 4, 5]))

    print(get_max_size_pos_sub_array(
        [8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575]
    )
    )
