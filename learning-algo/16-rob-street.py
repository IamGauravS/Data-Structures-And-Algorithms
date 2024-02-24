def max_subseq(arr,n):
    dp = [-1]*(n+1) 

    dp[0] = 0
    dp[1] = arr[0]

    for i in range(2, n+1):
        max_rece = dp[i-1]
        max_one_jump = dp[i-2] + arr[i-1]
        dp[i] = max(max_rece, max_one_jump)

    return dp[n]

def rob_street(arr, n):
    arr1 = []
    arr2 = []

    if n==1:
        return arr[0]
    
    for i in range(n):
        if i != 0:
            arr1.append(arr[i])
        if i != n-1:
            arr2.append(arr[i])

    amt1 = max_subseq(arr1, n-1)
    amt2 = max_subseq(arr2, n-1)

    return max(amt1, amt2)
