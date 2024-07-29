def contains_duplicate(nums):

    # Replace this placeholder return statement with your code
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
        
    return False
