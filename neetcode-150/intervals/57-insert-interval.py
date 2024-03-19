class Solution:
    
    def merge(self, intervals):
        stack = []
        stack.append(intervals[0])
        
        for i in range(1, len(intervals)):
            if stack[-1][1] >= intervals[i][0]:
                last_interval = stack.pop()
                new_interval_start = last_interval[0]
                new_interval_end = max(last_interval[1], intervals[i][1])
                
                stack.append([new_interval_start, new_interval_end])
                
            else:
                stack.append(intervals[i])
                
        return stack
                
                
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        if len(intervals) == 0:
            return [newInterval]
        
        i = 0
        flag = 0
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                flag = 1
                break 
          
        if flag == 0:
            i +=1
          
        index_to_insert = i 
        intervals.insert(index_to_insert, newInterval)
        
        output = self.merge(intervals)
        
        return output