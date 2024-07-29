def is_anagram(str1, str2):

    # Replace this placeholder return statement with your code
    if len(str1) != len(str2):
        return False
    str1_count_dict = {}
    for ch in str1:
        if ch not in str1_count_dict:
            str1_count_dict[ch] = 0
        str1_count_dict[ch] +=1
        
    for ch in str2:
        if ch not in str1_count_dict:
            return False 
        str1_count_dict[ch] -=1 
        
    for key, value in str1_count_dict.items():
        if value >0:
            return False
    
    return True
    
