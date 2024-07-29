class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_set = set(['+', '-', '*', '/'])
        
        for ch in tokens:
            if ch in operator_set:
                second_num = stack.pop()
                first_num = stack.pop()
                if ch == '+':
                    stack.append(first_num + second_num)
                elif ch == '-':
                    stack.append(first_num - second_num)
                elif ch == '*':
                    stack.append(first_num * second_num)
                else:  
                    stack.append(int(first_num / second_num))
                    
            else:
                stack.append(int(ch))
                
        return stack[0]
    
    
    
## optimal

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(x / y),  # use int() for truncating towards zero
        }
        
        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(), stack.pop()))
            else:  # token is a number
                stack.append(int(token))
        
        return stack[0]  # the result is the only element left in the stack