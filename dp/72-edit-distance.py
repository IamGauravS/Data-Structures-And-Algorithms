class Solution:
    def minDistanceHelper(self, index1, index2):
        
        
        if index1 == len(self.word1):
            return len(self.word2) - index2 
            
        
        if index2 == len(self.word2):
            return len(self.word1) - index1 
           
        
        if self.dp[index1][index2] != -1:
            return self.dp[index1][index2]

        if self.word1[index1] == self.word2[index2]:
            self.dp[index1][index2] = self.minDistanceHelper(index1+1, index2+1)

        else:
            self.dp[index1][index2] = 1 + min(self.minDistanceHelper(index1, index2+1), self.minDistanceHelper(index1+1, index2), 
                                          self.minDistanceHelper(index1+1, index2+1))
            
        return self.dp[index1][index2]


    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 and len(word2) == 0:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        self.dp = [[-1]*len(word2) for _ in range(len(word1))]
        self.word1 = word1 
        self.word2 = word2 

        self.minDistanceHelper(0, 0)

        return self.dp[0][0]