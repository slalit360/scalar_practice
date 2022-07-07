"""
Q4. Merge Intervals

Problem Description
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    # TC : O(n)
    if not intervals:
        return [newInterval]
    ans = []
    n = len(intervals)
    i = 0

    while i < n and intervals[i][1] < newInterval[0]:
        ans.append(intervals[i])
        i += 1

    s, e = newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        s = min(s, intervals[i][0])
        e = max(e, intervals[i][1])
        i += 1
    ans.append([s, e])

    while i < n:
        ans.append(intervals[i])
        i += 1
    return ans


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))
