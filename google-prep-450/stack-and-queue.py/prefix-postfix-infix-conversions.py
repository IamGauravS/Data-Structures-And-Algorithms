# Define precedence and associativity
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}

def is_operator(c):
    return c in precedence

def precedence_greater(op1, op2):
    return precedence[op1] > precedence[op2] if associativity[op1] == 'L' else precedence[op1] >= precedence[op2]

# Infix to Postfix Conversion
def infix_to_postfix(expression):
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':  # Left Parenthesis
            stack.append(char)
        elif char == ')':  # Right Parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '('
        else:  # Operator
            while (stack and stack[-1] != '(' and precedence_greater(stack[-1], char)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Infix to Prefix Conversion
def infix_to_prefix(expression):
    # Reverse the infix expression
    reversed_expr = expression[::-1]
    
    # Swap parentheses
    reversed_expr = reversed_expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    # Convert reversed infix to postfix
    postfix_expr = infix_to_postfix(reversed_expr)
    
    # Reverse postfix to get prefix
    return postfix_expr[::-1]

# Postfix to Infix Conversion
def postfix_to_infix(expression):
    stack = []
    
    for char in expression:
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            op1 = stack.pop()
            op2 = stack.pop()
            result = f'({op2}{char}{op1})'
            stack.append(result)
    
    return stack[0]

# Prefix to Infix Conversion
def prefix_to_infix(expression):
    stack = []
    
    # Traverse from right to left
    for char in expression[::-1]:
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            op1 = stack.pop()
            op2 = stack.pop()
            result = f'({op1}{char}{op2})'
            stack.append(result)
    
    return stack[0]

# Postfix to Prefix Conversion
def postfix_to_prefix(expression):
    stack = []
    
    for char in expression:
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            op1 = stack.pop()
            op2 = stack.pop()
            result = char + op2 + op1  # Combine in prefix form
            stack.append(result)
    
    return stack[0]

# Prefix to Postfix Conversion
def prefix_to_postfix(expression):
    stack = []
    
    # Traverse from right to left
    for char in expression[::-1]:
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            op1 = stack.pop()
            op2 = stack.pop()
            result = op1 + op2 + char  # Combine in postfix form
            stack.append(result)
    
    return stack[0]

