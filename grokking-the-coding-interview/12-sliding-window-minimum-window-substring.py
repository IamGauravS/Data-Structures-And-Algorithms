import sys
def min_window(str1, str2):
    
    # Replace this placeholder return statement with your code
    minimum_length = sys.maxsize 
    output_str = ""
    for i in range(len(str1)):
        k = 0
        l = i
        
        while  l < len(str1) and k < len(str2):
            if str1[l] == str2[k]:
                l+=1
                k+=1
            else:
                l+=1
                
        if k == len(str2):
            size = l -i 
            if size < minimum_length:
                minimum_length = size
                output_str = str1[i:l] 

    return output_str