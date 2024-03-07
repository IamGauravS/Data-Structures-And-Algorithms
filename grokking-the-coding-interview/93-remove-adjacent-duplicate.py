def remove_duplicates(string):

    # Replace this placeholder return statement with your code
    input_str = list(string)
    stack = []
    for s in input_str:
        if not stack or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()
    output = "".join(stack)
    return output
