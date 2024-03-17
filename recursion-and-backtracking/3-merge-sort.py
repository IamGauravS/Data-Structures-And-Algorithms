def merge(larr, rarr):
    i = j = 0
    output_arr = []
    while i < len(larr) and j < len(rarr):
        if larr[i] < rarr[j]:
            output_arr.append(larr[i])
            i += 1
        else:
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