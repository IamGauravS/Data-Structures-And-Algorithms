#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        This function returns the k most frequent elements in an array. We first create
        a dict to store the frequency for each element and then store them in an array as a 
        (-value, key) pair and finally use a heap to sort them. 

        Args:
        nums (List[int]) : input array
        k (int) : k elements that are required

        Returns:
        kFreqElements (List[int]) : output array containing k most freq elems
        """
        ## if there are no element we can return an empty array
        if len(nums) == 0:
            return []
        
        ## if number of elements in nums in less than k then we can return all the elements
        if len(nums) <= k:
            return list(set(nums))
        
        freqDict = defaultdict(int)  ## dictionary to store frequency elements

        for num in nums:
            freqDict[num] += 1

        ## heap to sort the elements by freq
        heap = []
        for key, value in freqDict.items():
            heap.append((-value, key))  ## we store -val since python has native implementation of min heap

        heapq.heapify(heap)

        kFreqElements = []  ## output array

        ## pop k elements or until heap is empty and store it in array
        while len(kFreqElements) < k and heap:
            kFreqElements.append(heapq.heappop(heap)[1])

        return kFreqElements


        
# @lc code=end

