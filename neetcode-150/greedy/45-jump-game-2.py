
class Solution:
    def jump(self, nums: List[int]) -> int:
        ## at update left pointer is left+1 and right is we can jump farthest

        noOfSteps = 0
        l = r = 0

        while r < len(nums)-1:
            farthest = 0

            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])

            l = r+1
            r = farthest
            noOfSteps += 1


        return noOfSteps        
        