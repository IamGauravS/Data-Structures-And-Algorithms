class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        lengths = [0] * N  # Store length of LIS ending at index i
        counts = [1] * N    # Store count of LISs ending at index i
        
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        
        max_length = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == max_length)
