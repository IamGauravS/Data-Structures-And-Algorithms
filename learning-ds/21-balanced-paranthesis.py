from Stack import MyStack

def is_balanced(exp):

    # Replace this placeholder return statement with your code
    compare_dict = {"{": "}", "[": "]", "(": ")"}
 
    stack = MyStack()
    for char in exp:
        if char in compare_dict:
            stack.push(char)
        else:
            if stack.is_empty():
                return False 
            val = stack.pop()
            if compare_dict[val] != char:
                return False 

    return True