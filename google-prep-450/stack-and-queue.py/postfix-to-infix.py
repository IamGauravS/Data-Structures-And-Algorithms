class Solution:
    def postfixToInfix(self, s):
        stack = []

        for ch in s:
            if ch.isalnum():
                stack.append(ch)

            else:
                op2 = stack.pop()
                op1 = stack.pop()

                newOperand = f"({op1}{ch}{op2})" 
                stack.append(newOperand)


        return stack[-1] if stack else ""
    

## postfix validity check

def isValidPostfix(postfix: str) -> bool:
    stack = 0  # Stack count (acts like a stack size indicator)
    
    for ch in postfix:
        if ch.isalnum():  # If it's an operand, increase stack size
            stack += 1
        else:  # If it's an operator
            if stack < 2:  # Not enough operands to apply the operator
                return False
            stack -= 1  # Applying the operator reduces the stack by one
    
    return stack == 1  # At the end, only one valid expression should remain in the stack

# Example usage:
postfix_expr = "ab+c*"
print(isValidPostfix(postfix_expr))  # True
