class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    
        if len(s)  != len(t):
            return False 
        
        hashTable = {}
        alreadyMapped = set()
        
        for i in range(len(s)):
            if s[i] not in hashTable and t[i] not in alreadyMapped:
                hashTable[s[i]] = t[i]
                alreadyMapped.add(t[i])
            else:
                if s[i] in hashTable and hashTable[s[i]] == t[i] :
                    continue
                else:
                    return False  

        return True 