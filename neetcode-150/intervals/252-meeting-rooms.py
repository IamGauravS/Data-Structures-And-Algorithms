class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        sortedIntervals = sorted(intervals)

        prevEnd = sortedIntervals[0][1]

        for start , end in sortedIntervals[1:]:
            if start < prevEnd:
                return False
            else:
                prevEnd = end 


        return True