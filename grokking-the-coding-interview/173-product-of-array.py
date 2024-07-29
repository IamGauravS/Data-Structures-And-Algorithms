def product_except_self(arr):

    # Replace this placeholder return statement with your code
    multiple_before_element = [1]
    
    curr_multiple = 1 
    for i in range(1, len(arr)):
        curr_multiple *= arr[i-1]
        multiple_before_element.append(curr_multiple)
        
    
    multiple_after_element = [1]
    reversed_arr = arr[::-1]
    curr_multiple = 1
    
    for i in range(1, len(reversed_arr)):
        curr_multiple *= reversed_arr[i-1]
        multiple_after_element.append(curr_multiple)
        
    multiple_after_element = multiple_after_element[::-1]
    
    output = []
    for i in range(len(arr)):
        output.append(multiple_after_element[i] * multiple_before_element[i])
        
    return output