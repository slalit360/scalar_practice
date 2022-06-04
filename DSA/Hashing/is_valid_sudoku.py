def isValidSudoku(A):
    N = len(A)
    br = 0
    bc = 0

    for i in range(9):
        # check rows
        hashset = set()
        for j in range(N):
            if A[i][j] in hashset:
                return 0
            elif A[i][j] != '.':
                hashset.add(A[i][j])
        # check cols
        hashset = set()
        for j in range(N):
            if A[j][i] in hashset:
                return 0
            elif A[j][i] != '.':
                hashset.add(A[j][i])

        # check box
        hashset = set()
        for j in range(3):
            for k in range(3):
                if A[br+j][bc+k] in hashset:
                    return 0
                elif A[br+j][bc+k] != '.':
                    hashset.add(A[br+j][bc+k])
        bc += 3
        # print("bc -> ", bc)
        if bc == 9:
            br += 3
            bc = 0
    return 1


if __name__ == '__main__':
    A = ["53..7....",
         "6..195...",
         ".98....6.",
         "8...6...3",
         "4..8.3..1",
         "7...2...6",
         ".6....28.",
         "...419..5",
         "....8..79"]
    print(isValidSudoku(A))
