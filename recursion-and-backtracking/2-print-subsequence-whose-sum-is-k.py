

def get_all_subset(input_arr, k, output, curr_index, curr_sum, temp):
    
    if curr_sum == k:
        output.append(temp[:])
        return 
    if curr_sum > k or curr_index == len(input_arr):
        return 
    
    
    temp.append(input_arr[curr_index])
    get_all_subset(input_arr, k, output, curr_index+1, curr_sum+input_arr[curr_index], temp)
    temp.pop()
    get_all_subset(input_arr, k, output, curr_index+1, curr_sum, temp)
        
    


def print_all_subsequence(input_arr, k):
    output = []
    
    get_all_subset(input_arr, k, output,0 ,0, [])
    return output