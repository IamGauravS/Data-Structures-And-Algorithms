class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = []
        suffixProducts = []

        numsLen = len(nums)

        currPrefixProd = 1
        currSuffixProd = 1

        for i in range(numsLen):
            prefixProducts.append(currPrefixProd)
            currPrefixProd = currPrefixProd*nums[i]

            suffixProducts.append(currSuffixProd)
            currSuffixProd = currSuffixProd*nums[numsLen-i-1]


        for i in range(numsLen):
            nums[i] = prefixProducts[i]*suffixProducts[numsLen-i-1]

        return nums


        
