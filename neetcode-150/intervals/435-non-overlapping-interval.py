class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        

        intervals = sorted(intervals) ## in python it sorts first by start value and then by end value
        prevEnd = intervals[0][1]
        noOfIntervals = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                
                prevEnd = end 

            else:
                noOfIntervals += 1
                prevEnd = min(end, prevEnd)

        return noOfIntervals