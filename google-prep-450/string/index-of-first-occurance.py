class Solution:
    def findMatching(self, text, pattern):
        # Code here
        if len(text) < len(pattern):
            return -1
            
        if len(text) == len(pattern):
            if text == pattern:
                return 0
            else:
                return -1
                
        for i in range(len(text) - len(pattern)+1):
            if text[i: i+len(pattern)] == pattern:
                return i
        
        return -1