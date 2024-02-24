from Stack import MyStack

def sort_stack(stack):
    
    # Replace this placeholder return statement with your code
    output_stack = MyStack()
    while not stack.is_empty():
        value = stack.pop()
        if output_stack.is_empty():
            output_stack.push(value)
        else:
            top = output_stack.peek()
            while top != None and top < value and not output_stack.is_empty():
                stack.push(output_stack.pop())
                top = output_stack.peek()

            output_stack.push(value)
    return output_stack