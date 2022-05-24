

def get_equilibrium_index(A):
    """
    Equilibrium index is an index where sum of elements at left indices is equal to
    sum of elements at right indices of array. such index where above condition is met is that index.
    """
    n = len(A)
    ps = [0] * n
    ps[0] = A[0]
    for i in range(1, n):
        ps[i] = ps[i-1] + A[i]

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


def equilibrium(arr):
    # finding the sum of whole array
    total_sum = sum(arr)
    leftsum = 0
    for i in range(len(arr)):

        # total_sum is now right sum
        # for index i
        total_sum -= arr[i]

        if leftsum == total_sum:
            return i
        leftsum += arr[i]

    # If no equilibrium index found,
    # then return -1
    return -1


if __name__ == '__main__':
    A = [-7, 1, 5, 2, -4, 3]
    get_equilibrium_index(A)
    print(equilibrium(A))