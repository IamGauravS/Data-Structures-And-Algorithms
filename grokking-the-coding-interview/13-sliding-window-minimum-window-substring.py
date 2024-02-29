import sys
def min_window(s, t):
    
    t_dict = {}
    s_dict = {}
    for ch in t:
        if ch not in t_dict:
            t_dict[ch] = 1
        else:
            t_dict[ch] +=1

    for ch in t:
        if ch in t_dict:
            s_dict[ch] = 0

    start = 0
    end = 0
   
    min_length = sys.maxsize
    min_window = ""
    for i in range(len(s)):
        if s[i] in t_dict:
            s_dict[s[i]] +=1

        while all(s_dict.get(ch) >= t_dict[ch] for ch in t_dict):
            length = i - start + 1
            if length < min_length:
                min_length = length
                min_window = s[start:i+1]
            if s[start] in t_dict:
                s_dict[s[start]] -= 1
            start += 1

    


    # Replace this placeholder return statement with your code
    return min_window