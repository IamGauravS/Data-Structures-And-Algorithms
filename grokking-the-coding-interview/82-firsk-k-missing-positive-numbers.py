import sys
def first_k_missing_numbers(arr, k):

    # Replace this placeholder return statement with your code
    len_arr = len(arr)
    find_max = -sys.maxsize
    for num in arr:
        if find_max < num:
            find_max = num 
            
    for i in range(len_arr, find_max+1):
        arr.append(-1)
       
    i = 0 
    while i < len(arr):
        while 0 < arr[i] <= len(arr) and   arr[i] -1 != i:
            temp = arr[i] -1 
            arr[i], arr[temp] = arr[temp], arr[i]
        i +=1
        
            
    missing_numbers = []
    for i , num in enumerate(arr):
        if i != num-1:
            missing_numbers.append(i+1)
            
    return missing_numbers
