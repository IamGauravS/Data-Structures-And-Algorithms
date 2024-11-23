#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        freq = Counter(tasks)
        
        # Max-Heap to store task frequencies (use negative to simulate max-heap)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        # Cooldown queue to manage tasks in cooldown
        cooldown = deque()
        
        time = 0
        while max_heap or cooldown:
            # Increment time
            time += 1
            
            # Execute task if available
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # Decrement task frequency
                if count < 0:  # If tasks are still left
                    cooldown.append((time + n, count))
            
            # Check if any task is ready to re-enter the heap
            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(max_heap, count)
        
        return time


        
# @lc code=end

