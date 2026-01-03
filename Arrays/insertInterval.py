from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curr = 0

        while curr < len(intervals) and intervals[curr][1] < newInterval[0]:
            res.append(intervals[curr])
            curr += 1

        while curr < len(intervals) and intervals[curr][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[curr][0])
            newInterval[1] = max(newInterval[1], intervals[curr][1])
            curr += 1

        res.append(newInterval)

        while curr < len(intervals):
            res.append(intervals[curr])
            curr += 1

        return res

s = Solution()
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))