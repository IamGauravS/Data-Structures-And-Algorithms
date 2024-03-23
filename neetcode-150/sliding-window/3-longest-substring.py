class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        presence_set = set()
        
        start = 0
        
        max_length = 0
        
        
        for i in range(len(s)):
            if s[i] not in presence_set:
                
                max_length = max(max_length, (i-start)+1)
                presence_set.add(s[i])
                
            else:
                while s[start] != s[i]:
                    presence_set.remove(s[start])
                    start +=1
                     
                start +=1
                
                
        return max_length
    
    
    
## more optimised

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        start = max_length = 0

        for i, char in enumerate(s):
            if char in index_map and start <= index_map[char]:
                start = index_map[char] + 1
            else:
                max_length = max(max_length, i - start + 1)

            index_map[char] = i

        return max_length