def next_greater_element(nums1, nums2):

    # Replace this placeholder return statement with your code
    stack = []
    dict = {}
    
    for num in nums2:
        while stack and stack[-1] < num:
            prev_num = stack.pop() 
            dict[prev_num] = num 
            
        stack.append(num)
        
    while stack:
        dict[stack.pop()] = -1
        
    return [dict[num] for num in nums1]
