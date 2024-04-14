class Solution:
    def  minDistanceHelper(self , w1Index, w2Index):
        if w1Index == self.word1Len:
            return self.word2Len - w2Index

        if w2Index == self.word2Len:
            return self.word1Len - w1Index

        if (w1Index, w2Index) in self.dp:
            return self.dp[w1Index, w2Index]

        ## if both characters are equal
        if self.word1[w1Index] == self.word2[w2Index]:
            self.dp[w1Index, w2Index] = self.minDistanceHelper(w1Index+1, w2Index+1)
            return self.dp[w1Index, w2Index]

        ## if both characters are not equal
        ## delete
        minOperations = float('inf')
        minOperations = min(minOperations, self.minDistanceHelper(w1Index+1, w2Index))
        ## insert
        minOperations = min(minOperations, self.minDistanceHelper(w1Index, w2Index+1))
        ## replace
        minOperations = min(minOperations, self.minDistanceHelper(w1Index+1, w2Index+1))

        self.dp[w1Index, w2Index] = 1 + minOperations
        return self.dp[w1Index, w2Index]
        
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1Len = len(word1)
        self.word2Len = len(word2)

        self.word1 = word1
        self.word2 = word2 
        self.dp = {}
        return self.minDistanceHelper(0,0)