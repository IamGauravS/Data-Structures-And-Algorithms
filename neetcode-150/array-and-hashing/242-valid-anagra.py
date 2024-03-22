class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict = {}
        
        if len(s) != len(t):
            return False 
        
        for ch in s:
            if ch not in count_dict:
                count_dict[ch] = 0
            count_dict[ch] +=1
            
        for ch in t:
            if ch not in count_dict or count_dict[ch] == 0:
                return False 
            
            count_dict[ch] -= 1
            
                
                
        return True
        