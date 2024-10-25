class Solution:
    def minimumNumberOfCoins(self, coins, sum):
        minimumNumberOfCoins = 0
        coins = sorted(coins, reverse=True)
        currValue = sum

        for coin in coins:
            if coin <= currValue:
                minimumNumberOfCoins += (currValue // coin)
                currValue = (currValue % coin)
            if currValue == 0:
                break 

        return minimumNumberOfCoins

