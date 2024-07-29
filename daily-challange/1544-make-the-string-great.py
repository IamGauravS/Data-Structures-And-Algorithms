class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if len(stack) != 0 and ((stack[-1].islower() and stack[-1].upper() == ch) or (stack[-1].isupper() and stack[-1].lower() == ch)):
                stack.pop()
            else:
                stack.append(ch)
            
            
        return "".join(stack)
            
            
## optimise

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
            
        return "".join(stack)