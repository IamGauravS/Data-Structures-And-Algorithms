class Solution:
    def numDistinctHelper(self, indexS, indexT):
        if  indexT >= len(self.T):
            return 1 
        
        if indexS >= len(self.S) :
            return 0
        
        if (indexS, indexT) in self.dp:
            return self.dp[(indexS, indexT)]
        
        noOfWays = 0
        if self.S[indexS] == self.T[indexT]:
            noOfWays += self.numDistinctHelper(indexS+1, indexT+1) 
        
        noOfWays += self.numDistinctHelper(indexS+1, indexT)
        self.dp[(indexS, indexT)] = noOfWays

        return self.dp[(indexS, indexT)]
        
    def numDistinct(self, s: str, t: str) -> int:
        self.S = s 
        self.T = t
        self.dp = {}

        return self.numDistinctHelper(0,0)



## tabulation

class Solution:
    
        
    def numDistinct(self, s: str, t: str) -> int:
        lenS = len(s)
        lenT = len(t)

        self.dp = [[0 for i in range(lenS+1)] for j in range(lenT+1)]

        for i in range(lenS+1):
            self.dp[-1][i] = 1 

        for i in range(lenT-1, -1, -1):
            for j in range(lenS-1, -1, -1):
                
                if t[i] == s[j]:
                    self.dp[i][j] += self.dp[i+1][j+1]

                self.dp[i][j] += self.dp[i][j+1]
            

        return self.dp[0][0]

        