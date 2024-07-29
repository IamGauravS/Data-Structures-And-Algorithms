class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        output = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            
            while start < end:
                if nums[i] + nums[start] + nums[end] == target:
                    output.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start +=1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    
                elif  nums[i] + nums[start] + nums[end] < target:
                    start = start + 1
                
                else:
                    end = end -1
                    
                    
        return output 