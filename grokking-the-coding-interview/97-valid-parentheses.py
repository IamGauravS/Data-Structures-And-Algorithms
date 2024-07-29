def is_valid(s):

    # Replace this placeholder return statement with your code
    p_dict = {')':'(', ']':'[', '}':'{'}
    
    stack = []
    
    for ch in s:
        if ch not in p_dict.keys():
            stack.append(ch)
        else:
            if not stack:
                return False
            last_elem = stack.pop()
            if p_dict[ch] != last_elem:
                return False 
            
    if stack:
        return False
    
    return True 
    
    