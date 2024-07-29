class Solution:
    def contains(self, count_t, hash_set):
        for key, value in count_t.items():
            if key in hash_set and hash_set[key] >= value:
                continue
            else:
                return False
        return True
                
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for ch in t:
            count_t[ch] = 1+ count_t.get(ch, 0)
            
        if len(s) < len(t):
            return ""
        
        start = 0
        output_str = ""
        hash_set = {}
        min_len = len(s) + 1
        
        for end in range(len(s)):
            hash_set[s[end]] = 1+ hash_set.get(s[end], 0)
            
            if end - start + 1 < len(t):
                continue 
            
            while self.contains(count_t, hash_set):
                 curr_len = end-start + 1
                 if curr_len < min_len:
                     min_len = curr_len
                     output_str = s[start:end+1]
                     
                 hash_set[s[start]] -= 1
                 start = start +1
                 
        return output_str if min_len <= len(s) else ""
                  
    
    
    
### optimised

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for ch in t:
            count_t[ch] = 1+ count_t.get(ch, 0)
            
        if len(s) < len(t):
            return ""
        
        hash_set_s = {}
        required = len(count_t)
        formed = 0
        start = 0
        end = 0 
        min_len = float('inf')
        min_window = ""
        
        while end < len(s):
            char = s[end]
            hash_set_s[char] = hash_set_s.get(char, 0) 
            
            if char in count_t and hash_set_s[char] == count_t[char]:
                formed +=1 
                
            while start <= end and formed == required:
                char = s[start]
                
                if start - end + 1 < min_len:
                    min_len = start - end + 1
                    min_window = s[start:end+1]
                    
                start = start +1
                hash_set_s[start] -= 1
                
                if char in count_t and hash_set_s[char] < count_t[char]:
                    formed -= 1
                    
            end +=1
            
            
        return min_window if min_len != float('inf') else ""