"""
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.

 A = [2, 1]
 4

 A = [5]
 5
"""


def get_min_cost(A):
    # O(n log n)
    A.sort(reverse=True)
    total = sum(A)
    ans = 0
    for i in A:
        ans += total
        total -= i

    return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    print(get_min_cost(A))
