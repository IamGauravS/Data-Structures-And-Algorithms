def single_number(nums):

    # Replace this placeholder return statement with your code
    result = 0
    for num in nums:
        result = result ^ num 
        
    return result
