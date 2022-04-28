# alternatively we can use array[::-1]   -> O(n)
from time_utility import timeit


@timeit
def reverse(arr, start, end):
    # optimized way -> (start+end)/2 iterations -> n/2 iteration -> O(n)
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end = end - 1
    return arr


@timeit
def reverse_builtin(arr, start, end):
    return arr[::-1]


if __name__ == '__main__':
    arr2d = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 3, 4, 4]
    ]
    for arr in arr2d:
        print(f"array : {arr} \t-> reverse 0 - n index : \t{reverse(arr.copy(), 0, len(arr) - 1)}")
        print(f"array : {arr} \t-> reverse from 0 - 2 index : \t{reverse(arr.copy(), 0, 2)}")

    print("\nreverse vs builtin reverse\n")
    arr = list(range(10 ** 7))
    reverse(arr.copy(), 0, len(arr) - 1)
    reverse_builtin(arr.copy(), 0, len(arr) - 1) # faster
"""
output:

Function 'reverse' executed in 0.00000000s
array : [1, 2, 3, 4, 5] 	-> reverse 0 - n index : 	[5, 4, 3, 2, 1]
Function 'reverse' executed in 0.00000000s
array : [1, 2, 3, 4, 5] 	-> reverse from 0 - 2 index : 	[3, 2, 1, 4, 5]
Function 'reverse' executed in 0.00000000s
array : [1, 2, 3, 3, 4, 4] 	-> reverse 0 - n index : 	[4, 4, 3, 3, 2, 1]
Function 'reverse' executed in 0.00000000s
array : [1, 2, 3, 3, 4, 4] 	-> reverse from 0 - 2 index : 	[3, 2, 1, 3, 4, 4]

reverse vs builtin reverse

Function 'reverse' executed in 0.81769323s
Function 'reverse_builtin' executed in 0.04699183s
"""
