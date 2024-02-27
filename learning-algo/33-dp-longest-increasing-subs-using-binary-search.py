# Function to perform binary search
def bisect_left(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        # If the middle element is less than x, narrow down to right half
        if a[mid] < x: 
            left = mid + 1
        # Else, narrow down to left half
        else: 
            right = mid
    # Return the position where x should be inserted to maintain sorted order
    return left

def longest_sub_using_binary(arr):
    n = len(arr)
    # Initialize temp array with the first element of arr
    temp = [arr[0]]
    # Initialize length of longest increasing subsequence
    length  =1 

    # Iterate over the elements of arr starting from the second element
    for i in range(1,n):
        # If the current element is greater than the last element of temp
        # it means we can extend the existing subsequence
        if arr[i] > temp[-1]:
            temp.append(arr[i])
            length +=1
        else:
            # If the current element is not greater than the last element of temp
            # it means we need to find a place for it in the temp array
            # where it can replace a number which is greater than or equal to itself.
            # This is done to maintain the possibility of future elements extending the subsequence.
            ind = bisect_left(temp, arr[i])
            temp[ind] = arr[i]

    # Return the length of longest increasing subsequence
    return length