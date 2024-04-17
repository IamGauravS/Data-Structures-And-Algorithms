class Solution:
    def checkValidString(self, s: str) -> bool:
        # Stacks to store indices of open brackets and asterisks
        open_brackets = []
        asterisks = []

        for i, ch in enumerate(s):
            # If current character is an open bracket, push its index onto the stack
            if ch == "(":
                open_brackets.append(i)
            # If current character is an asterisk, push its index onto the stack
            elif ch == "*":
                asterisks.append(i)
            # current character is a closing bracket ')'
            else:
                # If there are open brackets available, use them to balance the closing bracket
                if open_brackets:
                    open_brackets.pop()
                elif asterisks:
                    # If no open brackets are available, use an asterisk to balance the closing bracket
                    asterisks.pop()
                else:
                    # nnmatched ')' and no '*' to balance it.
                    return False

        # Check if there are remaining open brackets and asterisks that can balance them
        while open_brackets and asterisks:
            # If an open bracket appears after an asterisk, it cannot be balanced, return false
            if open_brackets.pop() > asterisks.pop():
                return False  # '*' before '(' which cannot be balanced.

        # If all open brackets are matched and there are no unmatched open brackets left, return true
        return not open_brackets


## dp solution here 0 means open
class Solution:
    def check(self,s,i,o,dp):
        
        if i==len(s):
            if o == 0:
                return True
            else:
                return False
            
        if dp[i][o]!=-1:
            return dp[i][o]
        
        if o<0 or o>len(s)//2:
            dp[i][o]= False

        elif s[i]=="(":
            dp[i][o]= self.check(s,i+1,o+1,dp)
        elif s[i]==")":
            dp[i][o]= self.check(s,i+1,o-1,dp)
        else:
            dp[i][o]= self.check(s,i+1,o+1,dp) or self.check(s,i+1,o-1,dp) or self.check(s,i+1,o,dp)
        return dp[i][o]
        
    def checkValidString(self, s: str) -> bool:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.check(s,0,0,dp)