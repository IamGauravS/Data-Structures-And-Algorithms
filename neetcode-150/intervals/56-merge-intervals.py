class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, lambda interval: intervals[0])
        stack = []
        stack.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if stack[-1][1] >= intervals[i][0]:
                last_interval = stack.pop()
                new_interval_start = min(last_interval[0], intervals[i][0])
                new_interval_end = max(last_interval[1], intervals[i][1])
                
                stack.append([new_interval_start, new_interval_end])
                
            else:
                stack.append(intervals[i])
                
        return stack