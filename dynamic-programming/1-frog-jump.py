
import sys

def frog_jump(stairs):
    dp = [sys.maxsize for i in range(len(stairs))]
    dp[0] = 0
    dp[1] = abs(stairs[1]-stairs[0])
    
    for i in range(2, len(stairs)):
        dp[i] = min(dp[i-1] + abs(stairs[i] - stairs[i-1]), dp[i-2] + abs(stairs[i] - stairs[i-2]))
        
    return dp[-1]
    
    