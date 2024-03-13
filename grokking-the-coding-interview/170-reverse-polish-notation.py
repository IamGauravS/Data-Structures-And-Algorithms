
import operator
def rpn(tokens):
    # Replace this placeholder return statement with your code
    stack = []
    op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    for ch in tokens:
        
        if ch in op:
            second_number = stack.pop()
            first_number = stack.pop()
            result = op[ch](first_number, second_number)
            stack.append(result)
        else:
            stack.append(int(ch))
            
    return int(stack[0])
