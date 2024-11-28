#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return list(set(nums))

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)

        output = []
        for value, key in heap:
            output.append(key)
        return output

        
        
# @lc code=end

