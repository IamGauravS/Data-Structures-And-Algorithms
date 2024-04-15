class Solution:
    def isMatchHelper(self, sIndex, pIndex):
        if sIndex >= len(self.s):
            for i in range(pIndex, len(self.pattern)):
                if self.pattern[i] != '*':
                    return False 
            return True 
            

        if pIndex >= len(self.pattern):
            return False
        
        if (sIndex, pIndex) in self.dp:
            return self.dp[(sIndex, pIndex)]
        
        if self.pattern[pIndex] == "." or self.pattern[pIndex] == self.s[sIndex]:
            self.dp[(sIndex, pIndex)] = self.isMatchHelper(sIndex+1, pIndex+1)
        
        elif self.pattern[pIndex] == "*":
            self.dp[(sIndex, pIndex)] = self.isMatchHelper(sIndex, pIndex+1) or self.isMatchHelper(sIndex+1, pIndex)
        
        else:
            self.dp[(sIndex, pIndex)] = self.isMatchHelper(sIndex, pIndex+1)

        return self.dp[(sIndex, pIndex)]
        

    def isMatch(self, s: str, p: str) -> bool:
        self.pattern = "" 
        self.dp = {}

        for i, ch in enumerate(p):
            if ch == '*' and i < len(p)-1 and p[i+1] == '*':
                continue 
            self.pattern += ch

        self.pattern = self.pattern[::-1]
        self.s = s[::-1]

        return self.isMatchHelper(0,0)