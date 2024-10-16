class Solution:
    def subarraysWithKDistinctHelper(self, nums, k):
        if k == 0:
            return 0

        start = 0
        numCount = {}
        count = 0

        for end in range(len(nums)):
            numCount[nums[end]] = numCount.get(nums[end], 0) + 1

            while len(numCount) > k:
                numCount[nums[start]] -= 1
                if numCount[nums[start]] == 0:
                    del numCount[nums[start]]
                start += 1
            
            count += end - start + 1

        return count
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithKDistinctHelper(nums, k) - self.subarraysWithKDistinctHelper(nums, k-1)
