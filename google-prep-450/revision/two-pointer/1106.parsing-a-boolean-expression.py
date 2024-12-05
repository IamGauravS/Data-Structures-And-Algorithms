#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch == ',':
                continue

            elif ch in ['t', 'f', '|', '&', '!']:
                stack.append(ch)

            elif ch == ')':
                values = []
                # Collect values until reaching the operator
                while stack[-1] not in ['&', '|', '!']:
                    values.append(stack.pop())
                operator = stack.pop()  # Pop the operator

                # Evaluate the result based on the operator
                if operator == '&':
                    result = all(val == 't' for val in values)
                elif operator == '|':
                    result = any(val == 't' for val in values)
                elif operator == '!':
                    # For '!', there should be exactly one value
                    result = values[0] == 'f'

                # Push the result back to the stack
                stack.append('t' if result else 'f')

        # The final result is on top of the stack
        return stack[-1] == 't'

        
# @lc code=end

