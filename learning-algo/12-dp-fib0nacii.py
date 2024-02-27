fb_array = [-1]*6

def fb_helper(fb_array, n):
    if n <2:
        fb_array[n] = n

    else:
        if fb_array[n-1] == -1:
            fb_helper(fb_array, n-1)
        if fb_array[n-2] == -1:
            fb_helper(fb_array, n-2)
        fb_array[n] = fb_array[n-1] + fb_array[n-2]


fb_helper(fb_array,5)
print(fb_array[5])
print(fb_array)

## this is a better solution
def fb_tabulation(n):
    if n<2:
        return n
    dp = [-1]*6
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def db_tabulation_space(n):
    if n<2:
        return n 
    prev, prev2 = 0,1
    for i in range(2, n+1):
        curr = prev + prev2 
        prev2 = prev 
        prev = curr 

    return curr 
# Here's how the indices map to the Fibonacci sequence:

# Index 0: Fibonacci number 0
# Index 1: Fibonacci number 1
# Index 2: Fibonacci number 1
# Index 3: Fibonacci number 2
# Index 4: Fibonacci number 3
# Index 5: Fibonacci number 5
# So, if you want the first 5 Fibonacci numbers, you need to calculate up to index 4, and if you want the first 6 Fibonacci numbers, you need to calculate up to index 5. That's why an array of size 6 is used in your code.