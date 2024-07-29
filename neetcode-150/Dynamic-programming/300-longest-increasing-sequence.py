class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp  = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  ## if longest increasing subsequence ends at nums[j] and if our current element
                    ## is greater than that then we can add it to that subsequence
                    ## we need to compare with all elements less than i bcoz we need to fnd the longest increasesing subsequence
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
    




        