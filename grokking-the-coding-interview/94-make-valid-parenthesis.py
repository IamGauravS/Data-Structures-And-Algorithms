def remove_indices(lst, indices):
    return [elem for i, elem in enumerate(lst) if i not in indices]

def min_remove_parentheses(s):
    
    # Replace this placeholder return statement with your code
    str_list = list(s)
    new_str = ""
    stack = []
    for index, ch in enumerate(str_list):
        if ch == ')':
            if stack and stack[-1][0] == '(':
                stack.pop()
            else:
                stack.append([ch, index])
        elif ch == '(':
            stack.append([ch, index])
        
    elements_to_remove = [elem[1] for elem in stack]
    
    str_list = remove_indices(str_list, elements_to_remove)
    return  ''.join(str_list)
            
    
    
        