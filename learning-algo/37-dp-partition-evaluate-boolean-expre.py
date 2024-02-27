## or -> | & -> and xpr -> ^ we have to evaluate the function in such a way that we can get true
## at every operand we can do a partition to solve the right and left sub problem
## pattern of breaking it down on the operand
## operand will always be at distance of 2 and start for 1 till j-1
## for and operatior total no of ways to yield true = left*right
## for or operator total no of ways to yield true = total true * total true + total false * total true + total true * total false
## for xor operator = total true * total false + total false * total true
## we need to find no of ways we can get true and no of ways we can get true 
## so we carry a third operator eg f(0,10, trur) or f(0,10, false)
import sys
def find_total_no_of_ways_we_get_true(arr, i, j, isTrue):
    if i>j: return 0  ## zero ways to get true or false 

    # If the start index is equal to the end index, it means we're looking at a single character
    # If we want the result to be true, return 1 if the character is 'T', 0 otherwise
    # If we want the result to be false, return 1 if the character is 'F', 0 otherwise
    if i==j:  ## it will either be true or false
        if isTrue ==1:
            return arr[i] == 'T'
        else:
            return arr[i] == 'F'
    
    max_no_of_ways = -1 *sys.maxsize
    for ind in range(i+1, j,2):
        LT = find_total_no_of_ways_we_get_true(arr, i, ind-1,1)
        LF = find_total_no_of_ways_we_get_true(arr, i, ind-1,0)
        RT = find_total_no_of_ways_we_get_true(arr, ind+1 ,j,1)
        RF = find_total_no_of_ways_we_get_true(arr, ind+1 ,j,0)

        if arr[ind] == '|':
            no_of_ways = LT*RT + LF*RT + LT*RF 
        elif arr[ind] == "&":
            no_of_ways = LT*RT 
        else :
            no_of_ways = LT*RF + LF*RT 
        
        if no_of_ways > max_no_of_ways:
            max_no_of_ways = no_of_ways

    return max_no_of_ways

        
def find_total_no_of_ways_we_get_true_dp(arr, i, j, isTrue, dp):
    if i>j: return 0  ## zero ways to get true or false 

    if i==j:  ## it will either be true or false
        if isTrue ==1:
            return arr[i] == 'T'
        else:
            return arr[i] == 'F'
    
    if dp[i][j][isTrue] != -1:
        return dp[i][j][isTrue]

    max_no_of_ways = 0
    for ind in range(i+1, j,2):
        LT = find_total_no_of_ways_we_get_true_dp(arr, i, ind-1,1, dp)
        LF = find_total_no_of_ways_we_get_true_dp(arr, i, ind-1,0, dp)
        RT = find_total_no_of_ways_we_get_true_dp(arr, ind+1 ,j,1, dp)
        RF = find_total_no_of_ways_we_get_true_dp(arr, ind+1 ,j,0, dp)

        if arr[ind] == '|':
            no_of_ways = LT*RT + LF*RT + LT*RF 
        elif arr[ind] == "&":
            no_of_ways = LT*RT 
        else :
            no_of_ways = LT*RF + LF*RT 
        
        max_no_of_ways += no_of_ways

    dp[i][j][isTrue] = max_no_of_ways
    return max_no_of_ways




arr = "T|F&T^T"
n = len(arr)
dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
result = find_total_no_of_ways_we_get_true_dp(arr, 0, n-1, 1, dp)
print(result)