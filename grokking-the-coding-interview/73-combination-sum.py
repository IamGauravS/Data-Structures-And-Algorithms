def combination_sum(nums, target):
    def backtrack(remain, combo, start):
        if remain == 0:
            result.append(list(combo))
            return
        elif remain < 0:
            return
        for i in range(start, len(nums)):
            combo.append(nums[i])
            backtrack(remain - nums[i], combo, i)
            combo.pop()

    result = []
    backtrack(target, [], 0)
    return result

### using dp

def combination_sum(nums, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # There is one way to make sum 0: no numbers

    for num in nums:
        for i in range(num, target + 1):
            for prev in dp[i - num]:  ## it will not run if dp[i-num] is empty
                dp[i].append(prev + [num])

    return dp[target]