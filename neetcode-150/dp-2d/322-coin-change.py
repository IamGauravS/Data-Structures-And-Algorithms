import sys

def recursion(target, coins, min_no_of_coins, no_of_coins, dp):
    if target == 0:
        return 1
    if target < 0:
        return 
    
    if dp[target] != -1:
        return dp[target]
    
    min_coin = sys.maxsize
    for coin in coins:
        if coin  <= target:
            recursion(target - coin, coins, min_no_of_coins, no_of_coins+1)
            
    return 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        target = amount
        min_no_of_coins = [sys.maxsize]
        dp = [-1 for i in range(target+1)]
        recursion(target, coins, min_no_of_coins, 0, dp)
        
        if min_no_of_coins[0] != sys.maxsize:
            return min_no_of_coins[0]
        else:
            return -1