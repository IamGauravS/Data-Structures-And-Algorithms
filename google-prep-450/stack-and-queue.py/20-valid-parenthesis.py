class Solution:
    def isValid(self, s: str) -> bool:
        count = 0

        stack = []

        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                openbracket = stack.pop()
                if (openbracket == '(' and ch == ')') or (openbracket == '[' and ch == ']') or (openbracket == '{' and ch == '}'):
                    continue 

                else:
                    return False

        if len(stack) == 0:
            return True

        return False