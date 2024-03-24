class Solution:
    def isValid(self, s: str) -> bool:
        key_dict = {')': '(', '}': '{', ']': '['}
        
        stack = []
        
        for ch in s:
            if ch not in key_dict:
                stack.append(ch)
            else:
                if stack and stack[-1] == key_dict[ch]:
                    stack.pop()
                else:
                    return False
                
        if stack:
            return False
        return True 