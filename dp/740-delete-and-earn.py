from collections import defaultdict

class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        uniqueNumList = sorted(list(set(nums)))
        lenList = len(uniqueNumList)
        numCounts = defaultdict(int)

        for num in nums:
            numCounts[num] += 1


        dp = [uniqueNumList[0]*numCounts[uniqueNumList[0]]]

        for i in range(1, lenList):
            currValue = uniqueNumList[i]

            currEarn = currValue*numCounts[currValue]

            if uniqueNumList[i] - uniqueNumList[i-1] == 1:
                dp.append(max(currEarn + (dp[i-2] if i >= 2 else 0), dp[i-1]))
            else:
                dp.append(currEarn + dp[i-1])


        return dp[-1]

        