

def get_equilibrium_index(arr):
    """
    Equilibrium index is an index where sum of elements at left indices is equal to
    sum of elements at right indices of array. such index where above condition is met is that index.
    :param arr:
    :return:
    """
    n = len(arr)
    ps = [0] * n
    ps[0] = arr[0]
    for i in range(1, n):
        ps[i] = ps[i-1] + arr[i]

    # print(ps)

    for i in range(n):
        if i < 1:
            sum_left = 0
        else:
            sum_left = ps[i-1]

        if i >= n-1:
            sum_right = 0
        else:
            sum_right = ps[n-1] - ps[i]

        if sum_left == sum_right:
            print(f"equilibrium index : {i}")


if __name__ == '__main__':
    A = [-7, 1, 5, 2, -4, 3]
    get_equilibrium_index(A)