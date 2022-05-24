"""
There are n people standing in a circle waiting to be executed.
The counting out begins at some point in the circle and proceeds around the circle in a fixed direction.
In each step, a certain number of people are skipped and the next person is executed.
The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed),
until only the last person remains, who is given freedom.
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle.
The task is to choose the place in the initial circle so that you are the last one remaining and so survive.
"""


# steps
# 1. unset the MSB bit (t)
# 2. return 2t+1
import math


def get_alive_position_1(N):
    count = 0
    n = N
    while n > 0:
        count += 1
        n = n >> 1
    t = N ^ (1 << count - 1)
    return 2 * t + 1


def get_alive_position_2(n, d=1):
    # 1. generate bits
    # 2. rotate right once
    pass


if __name__ == '__main__':
    for i in range(1, 20):
        print(i, get_alive_position_1(i))
        print(i, get_alive_position_2(i))
