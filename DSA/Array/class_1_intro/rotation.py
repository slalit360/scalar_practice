from DSA.Array.class_1_intro.reverse import reverse
from time_utility import timeit

"""
Rotate array k time either on left or right 
"""


@timeit
def left_rotate_by_slice(arr, k):
    n = len(arr)
    k = k % n
    if k > 0:
        arr = arr[k: n] + arr[0:k]
    return arr


@timeit
def right_rotate_by_slice(arr, k):
    n = len(arr)
    k = k % n
    if k > 0:
        arr = arr[-k: n] + arr[0:-k]
    return arr


@timeit
def left_rotate_one_by_one(arr, k):
    # => k * [1, n-1]
    # => k * n-1
    # => n * n-1
    # => O(n^2)
    n = len(arr)
    k = k % n
    for _ in range(k):
        tmp = arr[0]
        for i in range(1, n):
            arr[i - 1] = arr[i]
        arr[n - 1] = tmp
    return arr


@timeit
def right_rotate_one_by_one(arr, k):
    # => k * [n-1, 1]    1 - n + 1 + 1
    # => k * 3-n
    # => n * n
    # => O(n^2)
    n = len(arr)
    k = k % n
    for _ in range(k):
        tmp = arr[n - 1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = tmp
    return arr



@timeit
def left_rotate_by_reverse(arr, k):
    n = len(arr)
    k = k % n
    if k > 0:
        reverse(arr, 0, n - 1)
        reverse(arr, 0, n - 1 - k)
        reverse(arr, n - k, n - 1)
    return arr


@timeit
def right_rotate_by_reverse(arr, k):
    n = len(arr)
    k = k % n
    if k > 0:
        arr = reverse(arr, 0, n - 1)
        arr = reverse(arr, 0, k - 1)
        arr = reverse(arr, k, n - 1)
    return arr


if __name__ == '__main__':
    n = 10
    arr = list(range(1, n+1))  # [1, 2, 3, 4]
    k = 3
    print(f"Executing for n={n} and k={k}")
    print(f"Input array : {arr}" if n < 20 else "")

    if n > 20:
        left_rotate_one_by_one(arr.copy(), k)  # 2, 3, 4, 1
        left_rotate_by_slice(arr.copy(), k)  # 2, 3, 4, 1
        left_rotate_by_reverse(arr.copy(), k)  # 2, 3, 4, 1
        right_rotate_one_by_one(arr.copy(), k)  # 4, 1, 2, 3
        right_rotate_by_slice(arr.copy(), k)  # 4, 1, 2, 3
        right_rotate_by_reverse(arr.copy(), k)  # 4, 1, 2, 3
    else:
        print(left_rotate_one_by_one(arr.copy(), k))  # 2, 3, 4, 1
        print(left_rotate_by_slice(arr.copy(), k))  # 2, 3, 4, 1
        print(left_rotate_by_reverse(arr.copy(), k))  # 2, 3, 4, 1
        print(right_rotate_one_by_one(arr.copy(), k))  # 4, 1, 2, 3
        print(right_rotate_by_slice(arr.copy(), k))  # 4, 1, 2, 3
        print(right_rotate_by_reverse(arr.copy(), k))  # 4, 1, 2, 3


"""
output 2 : 

Executing for n=10 and k=3
Input array : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Function 'left_rotate_one_by_one' executed in 0.00000000s
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
Function 'left_rotate_by_slice' executed in 0.00099516s
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
Function 'left_rotate_by_reverse' executed in 0.00000000s
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
Function 'right_rotate_one_by_one' executed in 0.00000000s
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
Function 'right_rotate_by_slice' executed in 0.00000000s
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
Function 'right_rotate_by_reverse' executed in 0.00000000s
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

output 1 : 

Executing for n=10000000 and k=4

Function 'left_rotate_one_by_one' executed in 2.67658234s
Function 'left_rotate_by_slice' executed in 0.14864111s
Function 'left_rotate_by_reverse' executed in 1.35679317s
Function 'right_rotate_one_by_one' executed in 2.45563364s
Function 'right_rotate_by_slice' executed in 0.13773227s
Function 'right_rotate_by_reverse' executed in 1.30107141s


"""