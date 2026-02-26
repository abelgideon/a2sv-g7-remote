class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        L = 0

        for R in range(L, len(intervals) + 1):
            if R < len(intervals) and intervals[L][1] >= intervals[R][0]:
                intervals[L][1] = max(intervals[L][1], intervals[R][1])
                continue

            res.append([intervals[L][0], max(intervals[R-1][1], intervals[L][1])])
            L = R

        return res