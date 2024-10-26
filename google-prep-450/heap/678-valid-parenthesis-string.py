class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  # Minimum possible open parentheses
        high = 0  # Maximum possible open parentheses

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                if low > 0:
                    low -= 1
                high -= 1
            else:  # ch == '*'
                if low > 0:
                    low -= 1
                high += 1
            
            if high < 0:
                return False

        return low == 0
