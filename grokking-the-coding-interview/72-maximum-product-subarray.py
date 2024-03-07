def max_product(nums):
    dp = [[0 for _ in range(len(nums))] for _ in range(2)]
    dp[0][0] = dp[1][0] = nums[0]
    max_value = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            dp[0][i] = min(dp[1][i-1] * nums[i], nums[i])
            dp[1][i] = max(dp[0][i-1] * nums[i], nums[i])
        else:
            dp[0][i] = max(dp[0][i-1] * nums[i], nums[i])
            dp[1][i] = min(dp[1][i-1] * nums[i], nums[i])

        max_value = max(max_value, dp[0][i])

    return max_value