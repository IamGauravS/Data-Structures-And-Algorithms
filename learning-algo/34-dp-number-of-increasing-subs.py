def print_longest_increasing_subs(arr):
    n = len(arr)
    # Initialize the dp table with -1s. dp[i] will store the length of the longest increasing subsequence ending at index i.
    dp = [-1] * n
    # Initialize the count table with 1s. count[i] will store the number of longest increasing subsequences ending at index i.
    count = [1] * n 
    # Initialize the maximum length of increasing subsequence found so far.
    maxi = 1

    # Fill the dp and count tables
    for i in range(1, n):
        for j in range(i):
            # If arr[j] is less than arr[i] and the length of the longest increasing subsequence ending at index j + 1
            # is greater than the length of the longest increasing subsequence ending at index i, then update dp[i] and count[i].
            if arr[j] < arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                count[i] = count[j]
            # If arr[j] is less than arr[i] and the length of the longest increasing subsequence ending at index j + 1
            # is equal to the length of the longest increasing subsequence ending at index i, then update count[i].
            elif arr[j] < arr[i] and dp[i] == dp[j] + 1:
                count[i] += count[j]
        
        # Update the maximum length of increasing subsequence found so far.
        maxi = max(maxi, dp[i])

    # Calculate the total number of longest increasing subsequences.
    count_sum = 0
    for i in range(n):
        if dp[i] == maxi:
            count_sum += count[i]

    # Return the count table
    return count