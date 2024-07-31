class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPointer = 0
        current = 0
        twoPointer = len(nums) - 1

        while current <= twoPointer:
            if nums[current] == 0:
                nums[zeroPointer], nums[current] = nums[current], nums[zeroPointer]
                zeroPointer += 1
                current += 1
            elif nums[current] == 2:
                nums[twoPointer], nums[current] = nums[current], nums[twoPointer]
                twoPointer -= 1
            else:
                current += 1