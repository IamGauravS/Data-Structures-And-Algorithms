class Solution:
    def addOperators(self, num: str, target: int):
        # This function initiates the backtracking process
        result = []
        self.addOperatorsHelper(num, target, 0, '', 0, 0, result)
        return result

    def addOperatorsHelper(self, num, target, index, expression, current_value, previous_operand, result):
        # Base case: if we've reached the end of the string
        if index == len(num):
            # If the current value equals the target, add the expression to the result
            if current_value == target:
                result.append(expression)
            return

        # Try every possible split of the remaining string
        for i in range(index, len(num)):
            # Extract the current part of the string
            operand_str = num[index:i + 1]
            operand = int(operand_str)

            # Avoid numbers with leading zeros
            if i != index and num[index] == '0':
                break

            # If this is the first operand (i.e., starting point), initialize the expression
            if index == 0:
                self.addOperatorsHelper(num, target, i + 1, operand_str, operand, operand, result)
            else:
                # Try addition
                self.addOperatorsHelper(num, target, i + 1, expression + '+' + operand_str, current_value + operand, operand, result)

                # Try subtraction
                self.addOperatorsHelper(num, target, i + 1, expression + '-' + operand_str, current_value - operand, -operand, result)

                # Try multiplication
                self.addOperatorsHelper(num, target, i + 1, expression + '*' + operand_str, current_value - previous_operand + previous_operand * operand, previous_operand * operand, result)


