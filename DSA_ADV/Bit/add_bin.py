def addBinary(A, B):
    al = len(A)
    bl = len(B)

    if al > bl:
        B = B.zfill(al)
    else:
        A = A.zfill(bl)

    ans = ""
    carry = 0
    for i in range(max(al, bl)-1, -1, -1):
        summ = int(A[i]) + int(B[i]) + carry
        ans += str(summ % 2)
        carry = summ // 2
    if carry == 1:
        ans += "1"
    return ans[::-1]


if __name__ == '__main__':
    A = "000101011"
    B = "100001101"
    #    1001110001111010101001110
    #    0111001010101111000111001
    print(addBinary(A, B))