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
    


## chronological ordering

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms