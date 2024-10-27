#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        noOfIntervalsToBeRemoved = 0
        intervals = sorted(intervals, key = lambda x : x[1])
        prevEnd = intervals[0][1]

        i = 1
        while i < len(intervals):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]

            else:
                noOfIntervalsToBeRemoved += 1
                

            i += 1

        return noOfIntervalsToBeRemoved


# @lc code=end

