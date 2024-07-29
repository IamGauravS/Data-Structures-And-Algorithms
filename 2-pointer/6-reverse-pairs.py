

count = 0

def merge(larr, rarr):
    global count
    i = j = 0
    output_arr = []
    while i < len(larr) and j < len(rarr):
        if larr[i] < rarr[j]:
            output_arr.append(larr[i])
            i += 1
        else:
            
            if larr[i] > 2* rarr[j]:
                count += len(larr) - i  ## here we consider only one element in rarr and all elements in larray
                ## if the current element in larray is greater then twice of rarray then all the other remaining elements 
                ## in larray will also be greater since they are greater then current element
            output_arr.append(rarr[j])
            j += 1

    output_arr.extend(larr[i:])
    output_arr.extend(rarr[j:])

    return output_arr

def merge_sort(input_arr):
    if len(input_arr) <= 1:
        return input_arr

    mid = len(input_arr) // 2
    larr = merge_sort(input_arr[:mid])
    rarr = merge_sort(input_arr[mid:])

    return merge(larr, rarr)



def no_of_reverse_pairs(nums):
    ##a[i] > 2*a[j] and i< j
    
    global count 
    count = 0
    merge_sort(nums)
    
    return count 