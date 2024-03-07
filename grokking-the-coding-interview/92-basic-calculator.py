def calculate(s: str) -> int:
    def precedence(op: str) -> int:
        if op in {'+', '-'}:
            return 1
        return 0

    def apply_operator(operators: list, operands: list):
        operator = operators.pop()
        right_operand = operands.pop()
        left_operand = operands.pop()
        if operator == '+':
            operands.append(left_operand + right_operand)
        elif operator == '-':
            operands.append(left_operand - right_operand)

    operators = []
    operands = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            operands.append(num)
            continue
        elif s[i] == '(':
            operators.append(s[i])
        elif s[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, operands)
            operators.pop()  # Pop '('
        elif s[i] in {'+', '-'}:
            while operators and precedence(operators[-1]) >= precedence(s[i]):
                apply_operator(operators, operands)
            operators.append(s[i])
        i += 1

    while operators:
        apply_operator(operators, operands)

    return operands[-1]

