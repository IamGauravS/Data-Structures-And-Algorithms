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