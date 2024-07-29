def extra_character_index(str1, str2):
    result = 0
    str1_length = len(str1)
    str2_length = len(str2)
    
    
    for i in range(str1_length):
        result = result ^ (ord)(str1[i])
        
    for j in range(str2_length):
        result = result ^ (ord)(str2[j])
        
    if len(str1) > len(str2):
        index = str1.index((chr)(result))
        return index 
    else:
        index = str2.index((chr)(result))
        return index