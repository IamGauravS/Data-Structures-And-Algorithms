class Solution:
    def prefixToPostfix(self, prefix: str) -> str:
        stack = []

        # Traverse the prefix expression from right to left
        for ch in reversed(prefix):
            if ch.isalnum():  # If it's an operand (alphanumeric)
                stack.append(ch)
            else:  # If it's an operator
                # Pop two operands from the stack
                op1 = stack.pop()
                op2 = stack.pop()
                
                # Combine them into a postfix expression
                new_expr = f'{op1}{op2}{ch}'
                
                # Push the combined expression back onto the stack
                stack.append(new_expr)

        # The final postfix expression will be the only element in the stack
        return stack[-1]

# Example usage
sol = Solution()
prefix_expr = "*+ABC"
postfix_expr = sol.prefixToPostfix(prefix_expr)
print("Postfix expression:", postfix_expr)
