"""
A wire connects N light bulbs.

Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.


if we toggle any bulb, all bulbs to right will also toggled
"""


def get_min_switches_naive(A):
    # TC : O(n^2)
    # SC : O(1)
    count = 0
    n = len(A)
    for i in range(n):
        if A[i] == 0:
            for j in range(i, n):
                A[j] = A[j] ^ 1
            count += 1
    return count


def get_min_switches(A):
    # TC : O(n)
    # SC : O(1)
    count = 0

    for i in range(len(A)):
        if (A[i] == 0 and count % 2 == 0) or (A[i] == 1 and count % 2 == 1):
            count += 1
    return count


if __name__ == '__main__':
    A = [1, 0, 0, 1, 0]
    print(get_min_switches_naive(A.copy()))
    print(get_min_switches(A.copy()))
