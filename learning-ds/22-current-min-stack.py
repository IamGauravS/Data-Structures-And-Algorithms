from Stack import MyStack

class MinStack:
    # Initialize min and main stack here
    def __init__(self):
        self.main_stack = MyStack()
        self.min_stack = MyStack()
        # Write your code here
        

    # Remove and returns value from the stack
    def pop(self):

        self.min_stack.pop()
        return self.main_stack.pop()
        # Write your code here
        

    # Pushes values into the stack
    def push(self, value):

        # Write your code here
        self.main_stack.push(value)
        if self.min_stack.is_empty():
            self.min_stack.push(value)
        else:
            current_min = self.min_stack.peek()
            if current_min > value:
                self.min_stack.push(value)
            else:
                self.min_stack.push(current_min)

    # Returns minimum value from stack
    def min(self):

        # Write your code here
        return self.min_stack.peek()