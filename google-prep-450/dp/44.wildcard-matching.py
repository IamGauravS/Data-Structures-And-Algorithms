#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatchHelper(self, s, p, indexS, indexP):
        ## if we have reached successfully processed both input string and pattern
        if indexS == len(s) and indexP == len(p):
            return True 
        
        ## if we have reached the end of pattern but havent succefully processed the whole string then return false
        if indexP == len(p):
            return False 
        
        ## if we have reached the end of string retrn true if there is only 1 character left in pattern and it is * else false
        if indexS == len(s):
            if all(x == '*' for x in p[indexP:]):
                return True 
            else:
                return False 
            
        ## if we have already processed the current indexes
        if (indexS, indexP) in self.dp:
            return self.dp[(indexS, indexP)]

        if s[indexS] == p[indexP] or p[indexP] == '?':
            self.dp[(indexS, indexP)] = self.isMatchHelper(s, p, indexS+1, indexP+1)
        
        elif p[indexP] == '*':
            self.dp[(indexS, indexP)] = self.isMatchHelper(s, p, indexS+1, indexP) or self.isMatchHelper(s, p, indexS, indexP+1)
        
        else:
            self.dp[(indexS, indexP)] = False 

        return self.dp[(indexS, indexP)]


        
        
    def isMatch(self, s: str, p: str) -> bool:

        ## if both strings are empty return true
        if len(s) == 0 and len(p) == 0:
            return True 
        
        ## if pattern is empty but original string is not return False
        if len(p) == 0:
            return False 
         
        ## remove continuous ** from pattern since they are redundant
        prev = p[0]
        newPattern = p[0]

        for i in range(1, len(p)):
            if p[i] == '*':
                if prev == '*':
                    continue
                else:
                    newPattern += '*'
            else:
                newPattern += p[i]
                prev = p[i]

        ## if input string is empty
        if len(s) == 0:
            ## check if pattern only contains *
            if len(newPattern) == 1 and newPattern[0] == '*':
                return True 
            else:
                return False
        
        ## initialise dp array
        self.dp = {}

        ## call the helper function to do recursion
        self.isMatchHelper(s, newPattern, 0, 0)

        return self.dp[(0,0)]
            


         

        
# @lc code=end

