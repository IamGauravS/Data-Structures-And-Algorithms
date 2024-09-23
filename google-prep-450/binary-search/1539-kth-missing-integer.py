from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0] - 1:
            return k 
        
        currMissingNumber = k - (arr[0] - 1)

        for i in range(1, len(arr)):
            missingIntegers = arr[i] - arr[i-1] - 1

            if missingIntegers >= currMissingNumber:
                return arr[i-1] + currMissingNumber
            
            currMissingNumber -= missingIntegers

        return arr[-1] + currMissingNumber

##  optimised solution

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        low = 0
        high = len(arr) - 1

        while low <= high:
            pivot = (high + low) // 2

            if arr[pivot] - pivot - 1 < k:
                low = pivot + 1
            else:
                high = pivot - 1


        return low + k




