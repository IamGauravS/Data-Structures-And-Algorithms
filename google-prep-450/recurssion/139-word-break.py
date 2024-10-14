class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if s in self.memo:
            return self.memo[s]
        
        if len(s) == 0:
            return True 
        
        for word in wordDict:
            if len(word) <= len(s):
                if word == s[:len(word)]:
                    if self.wordBreak( s[len(word):], wordDict):
                        self.memo[s] = True
                        return True 
                    
        self.memo[s] = False 
        return False 
