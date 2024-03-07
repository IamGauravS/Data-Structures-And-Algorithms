def find_all_subsets_helper(nums, output_list, i, current_set):
    # Replace this placeholder return statement with your code
    if i >= len(nums):
        return output_list
    
    ### include the element in current set
    current_set.append(nums[i])
    output_list.append(list(current_set))
    find_all_subsets_helper(nums, output_list, i+1, current_set)
    
    ## not include the element in current set
    current_set.pop() 
    find_all_subsets_helper(nums, output_list, i+1, current_set)
    
    return output_list


def find_all_subsets(nums):
    output_list = [[]]
    currsent_set = []
    
    
    output_list = find_all_subsets_helper(nums, output_list, 0, currsent_set)
    
    return output_list
    