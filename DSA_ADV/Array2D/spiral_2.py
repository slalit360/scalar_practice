def generateMatrix(A):
    ans = [[0] * A for _ in range(A)]
    n = 1
    k = A
    r = 0
    c = 0
    while k > 1:
        for _ in range(k-1):
            ans[r][c] = n
            n += 1
            c += 1
        for _ in range(k-1):
            ans[r][c] = n
            n += 1
            r += 1
        for _ in range(k-1):
            ans[r][c] = n
            n += 1
            c -= 1
        for _ in range(k-1):
            ans[r][c] = n
            n += 1
            r -= 1
        r += 1
        c += 1
        k -= 2

    if k % 2 == 1:
        ans[r][c] = n

    return ans


if __name__ == '__main__':
    print(*generateMatrix(1), sep="\n")
