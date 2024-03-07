
import heapq

def find_sets(intervals):

    intervals = sorted(intervals)
    heap = []
    no_of_rooms = 0
    output = -1
    for interval in intervals:
        if len(heap) == 0:
            heapq.heappush(heap, interval[1])
            no_of_rooms += 1
        else:
            top_element = heap[0]   ## smalles element in the heap
            while heap and top_element <= interval[0]:  ## room can get empty at same time
                no_of_rooms -= 1
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            no_of_rooms += 1

        if output < no_of_rooms:
            output = no_of_rooms

    return output 