
# construct left max array, where
#   leftmax[i] => maximum value in array from index 0 to index i
def get_left_max(A):
    # TC : O(n)
    # SC : O(n)
    n = len(A)
    lm = [0] * n
    lm[0] = A[0]

    for i in range(1, n):
        lm[i] = max(lm[i-1], A[i])

    return lm


if __name__ == '__main__':
    A = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
    print(get_left_max(A))
