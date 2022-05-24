"""
There are N doors numbered from 1 to N, all off them are closed initially
A person is standing in front of every door
p1 will toggle 1, 2, 3, 4,....
p2 will toggle 2, 4, 6, 8,....
p3 will toggle 3, 6, 9, 12,....
pn will toggle nth door only

task : count the no of open door.
"""


def count_open_door(N):
    return int(N ** 0.5)


if __name__ == '__main__':
    print(count_open_door(110))
