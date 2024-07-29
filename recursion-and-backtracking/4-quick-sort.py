


def partition(input_arr, low, high):
    i = low -1
    pivot = input_arr[high]
    
    for j in range(low, high):
        if input_arr[j] <= pivot:
            i+=1
            input_arr[i], input_arr[j] = input_arr[j], input_arr[i]
            
    input_arr[i+1], input_arr[high] = input_arr[high], input_arr[i+1]
    return i+1 

def quick_sort(input_arr, low=0, high = None):
    if high is None:
        high = len(input_arr) -1 
    
    
    if low < high:
        pi = partition(input_arr, low, high)
        
        quick_sort(input_arr, low, pi-1)
        quick_sort(input_arr, pi+1, high)
        
    return input_arr
        