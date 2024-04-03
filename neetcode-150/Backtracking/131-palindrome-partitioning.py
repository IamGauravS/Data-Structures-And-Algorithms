class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, end, tmp):
            if start == end:
                res.append(tmp[:])
            for i in range(start, end):
                if s[start:i+1] == s[start:i+1][::-1]:
                    tmp.append(s[start:i+1])
                    backtrack(i+1, end, tmp)
                    tmp.pop()

        res = []
        backtrack(0, len(s), [])
        return res

    def checkPalindrome(self, currStr: str) -> bool:
        return currStr == currStr[::-1]
    
    
### optimised using dp

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = []
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

        def backtrack(start=0, path=[]):
            if start == n:
                res.append(path)
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end+1, path+[s[start:end+1]])
        
        backtrack()
        return res

