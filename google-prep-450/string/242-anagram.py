class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        charDictS = {}

        for i in range(len(s)):
            if s[i] not in charDictS:
                charDictS[s[i]] = 1
            else:
                charDictS[s[i]] += 1

            if t[i] not in charDictS:
                charDictS[t[i]] = -1 
            else:
                charDictS[t[i]] -= 1

        

        for key, value in charDictS.items():
            if value != 0:
                return False 
            
        return True

        