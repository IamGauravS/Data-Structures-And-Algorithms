def two_sum(arr, t):

    # Replace this placeholder return statement with your code
    target_dict = {}
    for i in range(len(arr)):
        
        diff = t - arr[i]
        if diff in target_dict:
            return [i, target_dict[diff]]
        else:
            target_dict[arr[i]] = i 
        
    
        
    