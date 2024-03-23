class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        
        hash_set_s1 = {}
        
        for ch in s1:
            hash_set_s1[ch] = 1 + hash_set_s1.get(ch, 0)
            
        start = 0
        hash_set_s2 = {}
        for end in range(len(s2)):
            
            hash_set_s2[s2[end]] = 1 + hash_set_s2.get(s2[end], 0)
            if end-start+1 < len(s1):
                continue
            
            if hash_set_s2 == hash_set_s1:
                return True 
            
            if end-start+1 == len(s1):
                hash_set_s2[s2[start]] -= 1
                if hash_set_s2[s2[start]] == 0:
                    del hash_set_s2[s2[start]]
                start +=1 
                
        return False
                
            
                