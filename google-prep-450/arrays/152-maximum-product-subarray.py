import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefixProd = 1
        suffixProd = 1

        maxProduct = -sys.maxsize

        for i in range(len(nums)):
            if prefixProd == 0:
                prefixProd = 1
            
            if suffixProd == 0:
                suffixProd = 1 

            prefixProd = prefixProd * nums[i]
            suffixProd = suffixProd * nums[len(nums)-1-i]

            maxProduct = max(maxProduct, prefixProd, suffixProd)


        return maxProduct





