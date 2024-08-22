class Solution:
    def threeSum(self, nums, target) -> List[List[int]]:
        result = []


        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue 

            left = i+1 
            right = len(nums)-1

            while left < right:
                if nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                
                elif nums[i] + nums[left] + nums[right] < target:
                    left += 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left+1 < len(nums) and nums[left] == nums[left+1]:
                        left += 1

                    while right-1 >= 0 and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1


        return result 
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue 

            tempResult = self.threeSum(nums[i+1:], target - nums[i])
            for res in tempResult:
                result.append(res+[nums[i]])

        return result 


