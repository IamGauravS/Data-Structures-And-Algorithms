class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0

        longestOnes = 0
        numberOfZeros = 0
        
        while end < len(nums):
            if nums[end] == 0:
                numberOfZeros += 1
                
            while numberOfZeros > k:
                if nums[start] == 0:
                    numberOfZeros -= 1
                    
                start += 1

            longestOnes = max(longestOnes, end - start + 1)
            end += 1

        return longestOnes
    


## slightly optimised

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        numberOfZeros = 0
        maxLength = 0
        
        for end in range(len(nums)):
            if nums[end] == 0:
                numberOfZeros += 1
                
            # Adjust the window when zeros exceed k
            while numberOfZeros > k:
                if nums[start] == 0:
                    numberOfZeros -= 1
                start += 1  # Shrink the window from the left
                
            # Update the maximum length of the valid window
            maxLength = max(maxLength, end - start + 1)

        return maxLength



      
