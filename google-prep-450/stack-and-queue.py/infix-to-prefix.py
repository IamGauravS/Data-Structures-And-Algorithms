class Solution:
    def __init__(self):
        # Operator precedence
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Infix to Postfix Conversion
    def infixToPostfixModified(self, s: str) -> str:
        ans = ""  # Output string
        stack = []  # Operator stack
        
        for ch in s:
            if ch.isalnum():  # For operands (handling both digits and letters)
                ans += ch
                
            elif ch == '(':  # Left parenthesis
                stack.append(ch)
                
            elif ch == ')':  # Right parenthesis
                while len(stack) > 0 and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()  # Remove the '(' from the stack
                
            else:  # Operator
                while (len(stack) > 0 and stack[-1] != '(' and 
                       ((self.priority[ch] < self.priority[stack[-1]]) or 
                        (self.priority[ch] == self.priority[stack[-1]] and ch != '^'))):
                    ans += stack.pop()
                stack.append(ch)

        # Pop remaining operators from the stack
        while len(stack) > 0:
            ans += stack.pop()

        return ans 

    # Infix to Prefix Conversion
    def infixToPrefix(self, s: str) -> str:
        # Step 1: Reverse the input string
        s = s[::-1]

        # Step 2: Swap parentheses
        s = s.replace('(', '#')  # Temporary swap for '('
        s = s.replace(')', '(')
        s = s.replace('#', ')')

        # Step 3: Convert the reversed string to postfix
        infixToPostfixResult = self.infixToPostfixModified(s)

        # Step 4: Reverse the postfix result to get prefix
        output = infixToPostfixResult[::-1]

        return output

# Example usage
sol = Solution()
print(sol.infixToPrefix("(A+B)*C"))
