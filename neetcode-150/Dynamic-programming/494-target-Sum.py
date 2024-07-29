class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = []
        dp.append(nums[0])
        dp.append(-nums[0])
        noOfWays = 0

        for i in range(1, len(nums)):
            tempDP = []
            for value in dp:
                
                tempDP.append(value+nums[i])
                tempDP.append(value-nums[i])
                

            dp = tempDP[:]


        for value in dp:
            if value == target:
                noOfWays += 1

        return noOfWays
            

## optimised

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  # base case we can reach zero in one way with no nums

        for num in nums:
            tempDP = collections.defaultdict(int)
            for sum, count in dp.items():
                tempDP[sum + num] += count
                tempDP[sum - num] += count
            dp = tempDP

        return dp[target]