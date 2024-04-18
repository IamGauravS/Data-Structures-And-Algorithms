class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumArray = sum(nums)
        lenArray = len(nums)

        sumExpected = ((lenArray)*(lenArray+1)) //2

        return sumExpected - sumArray