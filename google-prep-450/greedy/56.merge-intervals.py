#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key= lambda x : x[0])

        i = 1
        result = [intervals[0]]

        while i < len(intervals):
            prevIntervalStart = result[-1][0]
            prevIntervalEnd = result[-1][1]

            if intervals[i][0] <= prevIntervalEnd:
                result.pop()
                result.append([prevIntervalStart, max(prevIntervalEnd, intervals[i][1])])

            else:
                result.append(intervals[i])

            i += 1

        return result

            
            

# @lc code=end

