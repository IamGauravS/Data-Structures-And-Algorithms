import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        start = 0
        end = k 
        
        for i in range(start, end):
            heapq.heappush(heap, (-nums[i], i))
            
        while end < len(nums):
            curr = heap[0][1]
            
            while curr < start:
                heapq.heappop(heap)
                curr = heap[0][1]
                
            output.append(-heap[0][0])
            
            start +=1
            heapq.heappush(heap, (-nums[end], end))
            
            end +=1
          
        curr = heap[0][1]  
        while curr < start:
                heapq.heappop(heap)
                curr = heap[0][1]
                
        output.append(-heap[0][0])
        
        return output
        
        
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        output = []
        q = deque()  # stores indices
        
        for i in range(len(nums)):
            # remove elements out of the current window from the front of the queue
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # remove elements smaller than the current from the back of the queue
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            # the first element is the maximum in the current window
            if i >= k - 1:
                output.append(nums[q[0]])
        
        return output
            