def subsetsum(arr, target, ind, dp):
    if target ==0:
        return True 
    if ind == 0:
        return arr[ind] == target 
    
    if dp[ind][target] != -1:
        return dp[ind][target]
    
    nottaken = subsetsum(arr, target, ind -1, dp)
    taken = False
    if arr[ind] <= target:
        taken = subsetsum(arr, target-arr[ind], ind-1, dp)

    dp[ind][target] = taken or nottaken
    return dp[ind][target]

def subsetsum_main(n,k,arr):
    dp = [[-1 for i in range(k+1)] for i in range(n)] ## bcoz k+1 in index terms is k 

    return subsetsum(arr, k, n-1,dp)