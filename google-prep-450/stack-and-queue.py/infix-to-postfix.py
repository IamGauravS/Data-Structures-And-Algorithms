class solution:
    def __init__(self):
        self.priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def infixToPostfix(self, s):
        stack = []
        answer = "" 

        for ch in s:
            if ch.isdigit():
                answer += ch 

            elif ch == '(':
                stack.push(ch)

            elif ch == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    answer += stack.pop()
                    
                stack.pop()

            else:
                while len(stack) > 0 and self.priority.get(ch, 0) <= self.priority.get(stack[-1], 0):
                    answer += stack.pop()
                    
                stack.push(ch)


        while len(stack) > 0:
            answer += stack.pop()
            
        return answer

            