class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2*nums[j]:
                    result.append([nums[i], nums[j]])

        return len(result) 
    
class Solution:
    def mergeSort(self, low, high):
        if low >= high:
            return 0
        
        mid = (high+low)//2
        count = self.mergeSort(low, mid) + self.mergeSort(mid+1, high)

        i = low 
        j = mid+1

        while i <= mid and j <= high:
            if self.nums[i] > 2*self.nums[j]:
                count += mid-i+1
                j += 1
            else:
                i +=1

        self.nums[low:high+1] = sorted(self.nums[low:high+1])

        return count  


    def reversePairs(self, nums: List[int]) -> int:

        self.nums = nums.copy()
        return self.mergeSort(0, len(self.nums)-1)
        
    


