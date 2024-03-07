def counting_bits(n):
    
    # Replace this placeholder return statement with your code
    if n == 0:
        return [0]
    output_arr = [0 for i in range(n+1)]
    
    for i in range(1, n+1):
        output_arr[i] = output_arr[i//2] + i %2 
        
        
    return output_arr