def recursion(arr, output, curr_index, temp, curr_sum):
    
    if len(arr) == curr_index :
        output.append(curr_sum)
        return 
    
    temp.append(arr[curr_index])
    
    recursion(arr, output, curr_index+1, temp, curr_sum+arr[curr_index])
    temp.pop()
    recursion(arr, output, curr_index+1, temp, curr_sum)
    
    
def subset_sum(arr):
    
    output = []
    recursion(arr, output, 0, [], 0)
    
    return output