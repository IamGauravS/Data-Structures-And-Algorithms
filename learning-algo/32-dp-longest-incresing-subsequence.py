import sys
def find_length_increasing_subs(arr, index, prev):
    if index == n:
        return 0
    
    take = 0
    if prev < arr[index]:
        take = 1+find_length_increasing_subs(arr, index+1, prev=arr[index])

    not_take = find_length_increasing_subs(arr, index+1, prev)
    return max(take ,not_take)
    

def find_length_increasing_subs_dp(arr):
    n = len(arr)  # Get the length of the array
    
    # Initialize the dp table with 1s. This is because a single element is 
    # considered as an increasing subsequence of length 1.
    dp = [1 for _ in range(n)]
    prev = [-1] * n
    # Fill the dp table
    # Start from the second element (index 1) as the first element is already considered
    for i in range(1, n):
        # For each element at index i, check all the previous elements
        for j in range(i):
            # If the current element is greater than the previous element
            if arr[i] > arr[j]:
                # Update dp[i] if including the current element in the subsequence
                # results in a longer subsequence. This is done by comparing dp[i] 
                # and dp[j] + 1, where dp[j] + 1 represents the length of the 
                # subsequence ending at index j plus the current element.
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length of an increasing subsequence
    # This is done by returning the maximum value in the dp table, as dp[i] 
    # represents the length of the longest increasing subsequence ending at index i.
    print(dp)
    return max(dp)

def print_longest_increasing_subs_dp_with_pr(arr):
    n = len(arr)
    dp = [1] * n  # Initialize the dp table
    prev = [-1] * n  # Initialize the previous index table

    # Fill the dp table and the previous index table
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum length
    max_length_index = dp.index(max(dp))

    # Use the previous index table to print the longest increasing subsequence
    lis = []
    i = max_length_index
    while i != -1:
        lis.append(arr[i])
        i = prev[i]
    lis = lis[::-1]  # Reverse the list

    return lis

# Test the function with an example array
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(print_longest_increasing_subs_dp_with_pr(arr))  # Output: [10, 22, 33, 50, 60, 80]

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(find_length_increasing_subs_dp(arr)) 