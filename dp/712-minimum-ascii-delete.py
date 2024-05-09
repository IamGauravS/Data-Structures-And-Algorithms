class Solution:
    def minimumDeleteSumHelper(self, index1, index2):
        
        if index1 == len(self.s1):
            res = 0
            for i in range(index2, len(self.s2)):
                res += ord(self.s2[i])

            return res 

        if index2 == len(self.s2):
            res =0
            for i in range(index1, len(self.s1)):
                res += ord(self.s1[i])

            return res

        if self.dp[index1][index2] != -1:
            return self.dp[index1][index2]

        if self.s1[index1] == self.s2[index2]:
            self.dp[index1][index2] = self.minimumDeleteSumHelper(index1+1, index2+1)

        else:
            self.dp[index1][index2] = min( ord(self.s1[index1]) + self.minimumDeleteSumHelper(index1+1, index2) ,
                       ord(self.s2[index2]) + self.minimumDeleteSumHelper(index1, index2+1))
            
        return self.dp[index1][index2]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if len(s1) == 0 and len(s2) == 0:
            return 0

        self.dp = [[-1]*len(s2) for _ in range(len(s1))]

        self.s1 = s1
        self.s2 = s2 

        self.minimumDeleteSumHelper(0, 0)

        return self.dp[0][0]