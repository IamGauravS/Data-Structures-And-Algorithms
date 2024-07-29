




def recursion(arr, target, output, curr_index, temp, curr_sum):
    if curr_sum == target:
        output.append(temp[:])
    if len(arr) == curr_index or curr_sum > target:
        return 
    
    temp.append(arr[curr_index])
    
    recursion(arr, target, output, curr_index+1, temp, curr_sum+arr[curr_index])
    temp.pop()
    recursion(arr, target, output, curr_index+1, temp, curr_sum)
    
    
def combination_sum(arr, target):
    arr= sorted(arr)
    output = []
    recursion(arr, target, output, 0, [], 0)
    
    return output