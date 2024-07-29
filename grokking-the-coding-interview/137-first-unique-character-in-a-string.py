def first_unique_char(s):

    # Replace this placeholder return statement with your code
    freq_count = {}
    for ch in s:
        if ch not in freq_count:
            freq_count[ch] = 0
            
        freq_count[ch] +=1
        
    for i, ch in enumerate(s):
        if freq_count[ch] ==1:
            return i 
        
    return -1