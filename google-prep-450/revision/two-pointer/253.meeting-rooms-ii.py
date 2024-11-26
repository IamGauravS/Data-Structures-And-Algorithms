#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # Sort the intervals by their start time
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        minNumberOfrooms = 0

        # Use a priority queue to keep track of the end time of the meetings
        meetingQueue = []

        for interval in sortedIntervals:
            # If the current meeting starts after the earliest ending meeting, pop it from the queue
            if meetingQueue and meetingQueue[0] <= interval[0]:
                heapq.heappop(meetingQueue)

            # Push the current meeting's end time to the queue
            heapq.heappush(meetingQueue, interval[1])

            # The number of rooms needed is the size of the queue
            minNumberOfrooms = max(minNumberOfrooms, len(meetingQueue))

        return minNumberOfrooms
        
# @lc code=end

