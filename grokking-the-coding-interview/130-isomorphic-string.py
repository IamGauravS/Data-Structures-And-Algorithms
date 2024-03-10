def is_isomorphic(string1, string2):
  
    # Replace this placeholder return statement with your code
    mapping_dict1 = {}
    mapping_dict12 = {}
    
    for ch1, ch2 in zip(list(string1), list(string2)):
        if ch1 not in mapping_dict1:
            mapping_dict1[ch1] = ch2 
        else:
            if mapping_dict1[ch1] != ch2:
                return False 
        if ch2 not in mapping_dict12:
            mapping_dict12[ch2] = ch1 
        else:
            if mapping_dict12[ch2] != ch1:
                return False 
            
    return True