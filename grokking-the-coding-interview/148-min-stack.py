from stack import MainStack


class MinStack:
    # Initialize min and main stack here
    def __init__(self):

        # Write your code here
        self.stack = []
        self.min_stack = []

    # Remove and returns value from the stack
    def pop(self):

        # Write your code here
        if len(self.stack) <=0:
            return -1
        last_element = self.stack.pop()
        if last_element == self.min_stack[-1]:
            self.min_stack.pop()
        return last_element

    # Pushes values into the stack
    def push(self, value):

        # Write your code here
        self.stack.append(value)
        if not self.min_stack or value < self.min_stack[-1]:
            self.min_stack.append(value)

    # Returns minimum value from stack
    def min_number(self):

        # Write your code here
        if not self.min_stack:
            return None 
        return self.min_stack[-1]
