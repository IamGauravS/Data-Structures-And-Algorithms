def largest_increasing_subsequence(arr, n, curr_arr, max_len):
    if n>= len(arr):
        if len(curr_arr) > max_len[0]:
            max_len[0] = len(curr_arr)
        return

    if len(curr_arr) == 0:
        curr_arr.append(arr[n])
    else:
        if curr_arr[-1] < arr[n]:
            curr_arr.append(arr[n])
    
        largest_increasing_subsequence(arr, n+1, curr_arr, max_len)
        curr_arr.pop()
    largest_increasing_subsequence(arr, n+1, curr_arr, max_len)


max_len = [0]
largest_increasing_subsequence([5, 1, 7, 3, 8, 4, 9], 0, [], max_len)
print(max_len)