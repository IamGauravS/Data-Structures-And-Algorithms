class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)

        if numsSum % 2 == 1:
            return False
        
        targetSum = numsSum // 2

        dp = set()
        dp.add(0)

        for i in range(nums):
            nextDP = set()
            for t in dp:
                if t + nums[i] == targetSum:
                    return True 
                nextDP.add(t+nums[i])
                nextDP.add(t)   ## add previous dp value

            dp = nextDP 

        return True if targetSum in dp else False
            

        

def subsetSumUtil(ind, target, arr, dp):
    # Check if the target sum has been achieved.
    if target == 0:
        return True

    # If we have reached the first element in the array.
    if ind == 0:
        return arr[0] == target

    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]

    # Recursively try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)

    taken = False
    # Check if the current element can be taken without exceeding the target.
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)

    # Store the result in the dp array to avoid recomputation.
    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def subsetSumToK(n, k, arr):
    # Initialize a memoization table with -1.
    dp = [[-1 for j in range(k + 1)] for i in range(n)]

    # Call the utility function to find if a subset with the given target sum exists.
    return subsetSumUtil(n - 1, k, arr, dp)

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")


