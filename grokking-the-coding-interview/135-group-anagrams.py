def group_anagrams(strs):

    # Replace this placeholder return statement with your code
    def get_ord(ch):
        return ord(ch) - ord('a')
    
    anagram_dict = {}
    for s in strs:
        key = [0]*26
        for ch in s:
            key[get_ord(ch)] +=1 
        key = ''.join([str(num) for num in key])
        if key not in anagram_dict:
            anagram_dict[key] = []
            
        anagram_dict[key].append(s)
        
        
    output_list = []
    for key, value in anagram_dict.items():
        output_list.append(value)
        
    return output_list
