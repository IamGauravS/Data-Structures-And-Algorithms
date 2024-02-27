def Merge(left_list, right_list):
    output_list = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            output_list.append(left_list[i])
            i+=1
        else:
            output_list.append(right_list[j])
            j+=1 

    while i < len(left_list):
        output_list.append(left_list[i])
        i+=1
    while j < len(right_list):
        output_list.append(right_list[j])
        j+=1

    return output_list


def MergeSort(lst):
    if len(lst) <=1:
        return lst 
    
    mid = len(lst) // 2
    left_list = MergeSort(lst[:mid])
    right_list = MergeSort(lst[mid:])
    return Merge(left_list, right_list)


unsorted_list = [34, 7, 23, 32, 5, 6]
sorted_list = MergeSort(unsorted_list)
print(sorted_list)  # Output: [5, 6, 7, 23, 32, 34]