class Solution:
    def numDistinctHelper(self, indexS, indexT):
        if indexT == len(self.target):
            return 1
        if indexS == len(self.source):
            return 0

        if self.dp[indexS][indexT] != -1:
            return self.dp[indexS][indexT]
        
        noOfWays = self.numDistinctHelper(indexS+1, indexT)

        if self.source[indexS] == self.target[indexT]:
            noOfWays += self.numDistinctHelper(indexS+1, indexT+1) 

        self.dp[indexS][indexT] = noOfWays

        return noOfWays

    def numDistinct(self, s: str, t: str) -> int:
        self.source = s
        self.target = t
        self.dp = [[-1]*len(t) for _ in range(len(s))]

        return self.numDistinctHelper(0, 0)