class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        currMin, currMax = 1,1 

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue 

            tmp = currMax * n 
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tmp, n*currMin, n)
            
            res = max(currMax, res, currMin)


        return res


## better solution

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result  = -float('inf')

        currProd = 1

        for i in range(len(nums)):
            currProd = currProd*nums[i]
            result = max(currProd, result)
            if currProd == 0:
                currProd = 1

        currProd = 1

        for i in range(len(nums)-1, -1, -1):
            currProd = currProd*nums[i]
            result = max(currProd, result)
            if currProd == 0:
                currProd = 1


        return result