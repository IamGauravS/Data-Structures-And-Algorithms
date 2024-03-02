
import heapq
def find_kth_largest(nums, k):

    # Replace this placeholder return statement with your code
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap)> k:
            heapq.heappop(heap)
            
            
    return heap[0]