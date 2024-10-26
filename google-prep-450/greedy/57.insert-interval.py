#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1


        intervals.insert(i, newInterval)

        result = []
        i = 1
        result.append(intervals[0])

        while i < len(intervals):
            prevInterval = result[-1]
            prevIntervalStart = prevInterval[0]
            prevIntervalEnd = prevInterval[1]

            currIntervalStart = intervals[i][0]
            currIntervalEnd = intervals[i][1]

            if currIntervalStart <= prevIntervalEnd:
                result.pop()
                result.append([prevIntervalStart, max(prevIntervalEnd, currIntervalEnd)])
            else:
                result.append([currIntervalStart, currIntervalEnd])

            i += 1

        return result





# @lc code=end

