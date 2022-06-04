def get_count(A):
    """
    given an array of size n, find count of elements having one or more elements greater than itself.
    """
    n = len(A)

    maxx = A[0]
    for i in range(1, n):
        if A[i] > maxx:
            maxx = A[i]

    freq = 0
    for i in A:
        if i == maxx:
            freq += 1

    # pythonize way 1
    # _, freq = Counter(A).most_common(1)[0]

    # pythonize way 2
    # freq = A.count(max(A))

    return n - freq


if __name__ == '__main__':
    print(get_count([-3, -2, 6, 8, 4, 8, 5]))
