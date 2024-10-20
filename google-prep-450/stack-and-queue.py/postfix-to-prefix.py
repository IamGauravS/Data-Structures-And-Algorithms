class Solution:
    def postfixToPrefix(self, postfix: str) -> str:
        stack = []

        # Traverse the postfix expression from left to right
        for ch in postfix:
            if ch.isalnum():  # If it's an operand (alphanumeric)
                stack.append(ch)
            else:  # If it's an operator
                # Pop two operands from the stack
                op2 = stack.pop()
                op1 = stack.pop()
                
                # Combine them into a prefix expression with the operator before operands
                new_expr = f'{ch}{op1}{op2}'
                
                # Push the combined expression back onto the stack
                stack.append(new_expr)

        # The final prefix expression will be the only element in the stack
        return stack[-1]

# Example usage
sol = Solution()
postfix_expr = "AB+C*"
prefix_expr = sol.postfixToPrefix(postfix_expr)
print("Prefix expression:", prefix_expr)
