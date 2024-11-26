#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        interValsToRemove = 0

        intervals.sort(key=lambda x: x[1])

        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                interValsToRemove += 1

            else:
                prev = intervals[i]


        return interValsToRemove





        
# @lc code=end

