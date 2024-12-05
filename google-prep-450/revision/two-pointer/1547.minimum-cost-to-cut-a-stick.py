#
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#

# @lc code=start
class Solution:
    def minCostHelper(self, start, end, cuts):

        if end-start == 1:
            return 0

        if (start, end) in self.memDict:
            return self.memDict[(start, end)]

        minValue = float('inf')
        for cut in cuts:
            if start < cut < end:
                cost = (end-start) + self.minCostHelper(start, cut, cuts) + self.minCostHelper(cut, end, cuts)
                minValue = min(cost, minValue)

        self.memDict[(start, end)] = minValue if minValue != float('inf') else 0

        return self.memDict[(start, end)]


    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add boundaries to the cuts and sort them
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        # DP table to store the minimum cost for each subproblem
        dp = [[0] * m for _ in range(m)]

        # Iterate over the length of the subproblems
        for length in range(2, m):  # At least two boundaries are needed
            for i in range(m - length):
                j = i + length  # Endpoint of the subproblem
                dp[i][j] = float('inf')

                # Try every possible cut between i and j
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], cost)

        # The result is stored in dp[0][m-1]
        return dp[0][m - 1]

        
# @lc code=end

