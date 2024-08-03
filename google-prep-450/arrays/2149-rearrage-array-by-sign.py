class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posArray = []
        negArray  = []

        for num in nums:
            if num >= 0:
                posArray.append(num)
            else:
                negArray.append(num)

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = posArray[i // 2]
            else:
                nums[i] = negArray[i // 2]


        return nums