
def recursion(arr, target, curr_sum, temp, curr_index, output):
    if curr_sum == target:
        output.append(temp[:])
        return 
    if curr_index == len(arr) or curr_sum > target:
        return
    
    temp.append(arr[curr_index])
    recursion(arr, target, curr_sum + arr[curr_index], temp, curr_index, output)
    temp.pop()
    recursion(arr, target, curr_sum , temp, curr_index+1, output)
    return 



def combination_sum(arr, target):
    output = []
    recursion(arr, target, 0, [], 0, output)
    
    return output