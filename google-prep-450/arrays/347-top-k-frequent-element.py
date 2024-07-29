import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums 
        
        freqHeap = []

        freqCount = Counter(nums)

        for key, value in freqCount.items():
            heapq.heappush(freqHeap, (value, key))
            if len(freqHeap) > k:
                heapq.heappop(freqHeap)


        kFrequentElements = []

        for value, key in freqHeap:
            kFrequentElements.append(key)

        return kFrequentElements

