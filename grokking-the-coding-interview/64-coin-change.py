def coin_change(coins, total):
    # Replace this placeholder return statement with your code
    dp = [[float('inf') for i in range(len(coins) +1)] for j in range(total+1)]
    for j in range(len(coins) + 1):
        dp[0][j] = 0
    
    for i in range(1, total+1):
        for j in range(1, len(coins)+1):
            value_of_curr_coin = coins[j-1]
            if value_of_curr_coin > i:
                dp[i][j] = dp[i][j-1]
            else:
                
                dp[i][j] = min(dp[i][j-1],1+ dp[i-coins[j-1]][j])
                
                
    return dp[total][len(coins)] if dp[total][len(coins)] != float('inf') else -1
        
        
        
### optimised
def coin_change(coins, total):
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1