def singleNumberOccurrence(A):
    """
    Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

    NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    :param A:
    :return:
    """
    ans = 0
    for i in range(len(A)):
        ans ^= A[i]
    return ans


def addBinary(A, B):
    """
    Given two binary strings, return their sum (also a binary string).
    :param A:
    :param B:
    :return:
    """
    a_len = len(A)
    b_len = len(B)

    n = max(a_len, b_len)

    if a_len > b_len:
        B = '0' * (a_len - b_len) + B
    else:
        A = '0' * (b_len - a_len) + A

    i = n - 1
    carry = 0
    res = ''

    while i >= 0:
        carry_sum = carry + int(A[i]) + int(B[i])
        res = str(carry_sum % 2) + res
        carry = carry_sum // 2
        i -= 1
    if carry == 1:
        res = '1' + res
    return res


def count_set_bits(A):
    """
    Write a function that takes an integer and returns the number of 1 bits it has.
    :param A:
    :return:
    """
    num = A
    count = 0
    while num > 0:
        if num % 2 == 1:
            count += 1
        num = num // 2
    return count


if __name__ == '__main__':
    A = [5, 2, 3, 2, 3]
    print(singleNumberOccurrence(A))

    # A = "100"
    # B = "111"
    # addBinary(A, B)
