import sys
def find_max_knapsack_profit(capacity, weights, values):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            notake = dp[i-1][j]
            take = 0
            if weights[i-1] <= j:
                take = values[i-1] + dp[i-1][j-weights[i-1]]
            dp[i][j] = max(take, notake)
    
    return dp[len(weights)][capacity]
