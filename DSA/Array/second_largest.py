import math


def second_largest(arr):
    """
    return second max element present in array/list
    :param arr: array / list of elements
    :return: second largest element if exist else return -1 (when not found)
    """
    if len(arr) < 2:
        return -1
    max1 = max2 = -math.inf
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif max2 < i < max1:
            max2 = i
    if max2 == -math.inf:
        max2 = max1
    return max2


if __name__ == '__main__':
    arr2d = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 3, 4, 4],
        [2],
        []
    ]
    for arr in arr2d:
        print(f"array : {arr} -> second largest : {second_largest(arr)}")
