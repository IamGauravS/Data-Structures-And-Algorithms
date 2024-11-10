from typing import List

class Solution:
    def memoization(self, index, target, arr, memoryDict):
        MOD = 10**9 + 7
        
        if target == 0:
            return 1  # Found a valid subset with the exact sum
        if index == 0:
            return 1 if arr[0] == target else 0  # Base case: single element matches the target

        if (index, target) in memoryDict:
            return memoryDict[(index, target)]
        
        # Exclude current element
        ways = self.memoization(index - 1, target, arr, memoryDict) % MOD
        
        # Include current element, if possible
        if arr[index] <= target:
            ways += self.memoization(index - 1, target - arr[index], arr, memoryDict) % MOD
        
        memoryDict[(index, target)] = ways % MOD
        return memoryDict[(index, target)]
        
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        totalSum = sum(arr)
        
        # If totalSum + d is odd or target < 0, there's no valid subset partition
        if (totalSum + d) % 2 != 0 or totalSum < d:
            return 0
        
        target = (totalSum + d) // 2
        memoryDict = {}
        
        return self.memoization(n - 1, target, arr, memoryDict)
