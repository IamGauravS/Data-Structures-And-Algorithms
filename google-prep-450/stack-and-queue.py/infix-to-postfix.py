class Solution:
    def __init__(self):
        # Operator precedence
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        # Associativity (left or right)
        self.associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}  # 'L' = left, 'R' = right

    def infixToPostfix(self, s: str) -> str:
        stack = []
        answer = ""

        for ch in s:
            if ch.isdigit():  # If it's an operand (digit), add it to output
                answer += ch

            elif ch == '(':  # Left parenthesis, push to stack
                stack.append(ch)

            elif ch == ')':  # Right parenthesis, pop until left parenthesis
                while len(stack) > 0 and stack[-1] != '(':
                    answer += stack.pop()
                stack.pop()  # Pop the '('

            else:  # Operator
                # Pop from stack while operators have greater or equal precedence (for left-associative operators)
                while (len(stack) > 0 and stack[-1] != '(' and
                       (self.priority[ch] < self.priority[stack[-1]] or
                        (self.priority[ch] == self.priority[stack[-1]] and self.associativity[ch] == 'L'))):
                    answer += stack.pop()

                # Push the current operator onto the stack
                stack.append(ch)

        # Pop any remaining operators from the stack
        while len(stack) > 0:
            answer += stack.pop()

        return answer

# Example usage:
sol = Solution()
print(sol.infixToPostfix("(21+23)*34"))  # Example input
