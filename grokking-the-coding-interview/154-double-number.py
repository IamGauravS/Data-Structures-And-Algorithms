def two_single_numbers(arr):

    # Replace this placeholder return statement with your code
    bitwise_sum = 0
    for i in arr:
        bitwise_sum = bitwise_sum ^ i 
        
    bitwise_mask = bitwise_sum & (-bitwise_sum)
    results = 0
    
    for i in arr:
        if bitwise_mask & i:
            results = results ^ i 
            
    return [results, bitwise_sum ^ results]
