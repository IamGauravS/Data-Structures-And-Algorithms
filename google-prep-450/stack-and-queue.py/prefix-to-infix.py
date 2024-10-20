class Solution:
    def prefixToInfix(self, s):
        stack = []

        for ch in reversed(s):
            if ch.isalnum():
                stack.append(ch)

            else:
                op1 = stack.pop()
                op2 = stack.pop()

                newOperand = f"({op1}{ch}{op2})"

                stack.append(newOperand)


        return stack[-1]
    

    def checkIfValidPrefix(self, s):
        
        stack = 0  # Stack count (acts like a stack size indicator)

        # Traverse from right to left
        for ch in reversed(s):
            if ch.isalnum():  # If it's an operand, increase stack size
                stack += 1
            else:  # If it's an operator
                if stack < 2:  # Not enough operands to apply the operator
                    return False
                stack -= 1  # Applying the operator reduces the stack by one

        return stack == 1  # At the end, only one valid expression should remain in the stack


