import sys
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = -1 

        for i in range(len(nums)-1):  ## the point from where we want to change breakpoint
            if nums[i] < nums[i+1]:
                pointer = i 


        if pointer >= 0:  ## we want someone which is greater than current but the smallest of all of them 
            ## draw a graph since we know it is increasing the first one will be the answer from behind or last 
            ## in our case since we are starting from front
            j = len(nums)-1
            while nums[j] <= nums[pointer]:
                j -=1

            nums[pointer], nums[j] = nums[j], nums[pointer]

        left = pointer + 1
        right = len(nums)-1

        while left < right: ## we just need to do this since the point before is monotonically incresing
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        
        return 