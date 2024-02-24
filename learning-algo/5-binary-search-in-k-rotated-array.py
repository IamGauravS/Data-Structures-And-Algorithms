def find_pivot(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left+right) //2 

        if arr[mid] > arr[right]:
            left = mid + 1 

        else:
            right = mid 

    return left 

def binary_search(arr, k):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            return True 
        if arr[mid] > k:
            high = mid 

        else:
            low = mid+1 

    return False 


def find_in_k_rotated_array(arr, k):
    
    pivot = find_pivot(arr)
    first_array = arr[:pivot]
    second_array = arr[pivot:]
    return (binary_search(first_array, k) or binary_search(second_array, k))

