
def get_all_subset(arr, index, cur_arr):
    if index >= len(arr):
        print(cur_arr)
        return 
    
    cur_arr.append(arr[index])
    get_all_subset(arr, index+1, cur_arr)
    cur_arr.pop()
    get_all_subset(arr, index+1, cur_arr)

    
def print_all_subsequence_whose_some_k(arr, index, curr_arr,k):
    if index >= len(arr):
        return 
    
    
    curr_arr.append(arr[index])
    if sum(curr_arr) == k:
        print(curr_arr)
    print_all_subsequence_whose_some_k(arr, index+1, curr_arr,k)
    curr_arr.pop()
    print_all_subsequence_whose_some_k(arr, index+1, curr_arr,k)


print_all_subsequence_whose_some_k([1,4,6,2,3,5,4,6,-10,10], 0, [], 10)

    