class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        intervals = []
        for s, e in zip(start, end):
            intervals.append([s, e])
            
        intervals = sorted(intervals, key=lambda x: x[1])
        
        noOfMeetings = 0
        
        prevEnd = intervals[0][0]
        
        for i in range(1, len(intervals)):
            if prevEnd < intervals[i][0]:
                noOfMeetings += 1
                prevEnd = intervals[i][1]
                
        return noOfMeetings