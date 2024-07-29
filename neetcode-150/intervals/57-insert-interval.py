class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        intervals.insert(i, newInterval)

        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            lastInterval = stack[-1]
            if lastInterval[1] >= intervals[i][0]:
                stack[-1][1] = max(lastInterval[1], intervals[i][1])
            else:
                stack.append(intervals[i])

        return stack