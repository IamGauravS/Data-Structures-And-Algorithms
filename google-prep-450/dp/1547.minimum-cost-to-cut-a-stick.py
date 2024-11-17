#
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#

# @lc code=start
class Solution:
    def minCostHelper(self, start, end):
        # Base case: no cuts in this segment
        if start > end:
            return 0

        if (start, end) in self.memory:
            return self.memory[(start, end)]
        
        minCost = float('inf')

        # Try making a cut at every position in the current segment
        for ind in range(start, end + 1):
            cost = (
                self.cuts[end + 1] - self.cuts[start - 1]
                + self.minCostHelper(start, ind - 1)
                + self.minCostHelper(ind + 1, end)
            )
            minCost = min(minCost, cost)  

        self.memory[(start, end)] = minCost
        return minCost
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()

        dp = [[0]*len(cuts) for _ in range(len(cuts))]

        for start in range(len(cuts) - 2, 0, -1 ):
            for end in range(1, len(cuts)-1):
                if start > end:
                    continue
                minCost = float('inf')

                for ind in range(start, end + 1):
                    cost = (
                        cuts[end + 1] - cuts[start - 1]
                        + dp[start][ind - 1]
                        + dp[ind + 1][end]
                    )
                    minCost = min(minCost, cost)

                dp[start][end] = minCost

        return dp[1][len(cuts)-2]

    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add boundaries to the cuts and sort them
        cuts = [0] + cuts + [n]
        cuts.sort()
        self.cuts = cuts

        # Initialize memoization
        self.memory = {}

        # Compute the minimum cost
        return self.minCostHelper(1, len(cuts) - 2)

        
# @lc code=end

