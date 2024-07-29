def longest_palindrome(s):
    if len(s) == 0:
        return 0
    count_dict = {}
    
    for ch in s:
        if ch not in count_dict:
            count_dict[ch] = 0 
        count_dict[ch] +=1 
        
    max_length = 0
    has_odd = False
    for value in count_dict.values():
        if value % 2 == 0:
            max_length += value 
        else:
            max_length += value - 1
            has_odd = True
                
    if has_odd:
        max_length += 1
        
    return max_length