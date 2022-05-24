"""
Mod String
You are given a large number in the form of a string A where each character denotes a digit of the number.
You are also given a number B. You have to find out the value of A % B and return it.

A = "143"
B = 2
O = 1

A = "43535321"
B = 47
O = 20


"""


def findMod(self, A, B):
    # return int(A) % B

    ans = 0
    mod = B
    n = len(A)
    curr = 1
    for i in range(n - 1, -1, -1):
        dig = ord(A[i]) - 48  # ord('0')
        term = (dig * curr) % mod
        ans = (ans + term) % mod
        curr = (curr * 10) % mod
    return ans


if __name__ == '__main__':
    print(findMod("43535321", 47))
