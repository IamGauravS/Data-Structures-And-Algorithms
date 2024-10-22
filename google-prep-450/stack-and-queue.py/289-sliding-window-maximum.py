from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Deque to store indices of elements in decreasing order
        res = []  # Result list to store the maximums

        # Process the first k elements (first window)
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()  # Pop smaller elements from the deque
            dq.append(i)  # Append the current element index

        # Add the maximum for the first window
        res.append(nums[dq[0]])

        # Process the rest of the array
        for i in range(k, len(nums)):
            # Remove elements from the deque if they are out of the current window
            if dq[0] < i - k + 1:
                dq.popleft()
            
            # Maintain the decreasing order in deque
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)  # Append the current element index

            # Append the current maximum element (front of the deque)
            res.append(nums[dq[0]])

        return res

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