### in this question we can buy and sell stock any number of times but u can only sell if u have bought
## express everything in terms of index
## we have two cases we can buy or sell at each step, but if we have bought u can either sell or hold 
## take the maximum of all profits made

def when_to_buy_and_sell(price_list, buy_sell_flag, index):
    # Base case: if all prices have been considered, return 0
    if index == len(price_list):
        return 0

    # If a stock hasn't been bought yet
    if buy_sell_flag == False:
        # Consider the case where we buy the stock
        # Subtract the price from the maximum profit that can be made from the remaining prices after buying
        profit_buy = -1*(price_list[index]) + when_to_buy_and_sell(price_list, True, index+1)
        
        # Consider the case where we don't buy the stock
        # The maximum profit is the maximum profit that can be made from the remaining prices without buying
        profit_dont_buy = when_to_buy_and_sell(price_list, False, index+1)
        
        # Return the maximum profit that can be made from these two cases
        return max(profit_buy, profit_dont_buy)

    # If a stock has been bought
    if buy_sell_flag == True:
        # Consider the case where we sell the stock
        # Add the price to the maximum profit that can be made from the remaining prices after selling
        profit_sell = price_list[index] + when_to_buy_and_sell(price_list, False, index+1)
        
        # Consider the case where we don't sell the stock
        # The maximum profit is the maximum profit that can be made from the remaining prices without selling
        profit_dont_sell= when_to_buy_and_sell(price_list, True, index+1)
        
        # Return the maximum profit that can be made from these two cases
        return max(profit_sell, profit_dont_sell)
    
def when_to_buy_and_sell(price_list):
    n = len(price_list)
    
    # Initialize the dp table
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    
    # Fill the dp table
    for i in range(n-1, -1, -1):
        for flag in range(2):
            # If a stock hasn't been bought yet
            if flag == 0:
                # Consider the case where we buy the stock
                # Subtract the price from the maximum profit that can be made from the remaining prices after buying
                # If we're on the last day, the profit from buying is 0 because we can't buy a stock on the last day
                profit_buy = -price_list[i] + dp[i+1][1] if i < n-1 else 0
                
                # Consider the case where we don't buy the stock
                # The maximum profit is the maximum profit that can be made from the remaining prices without buying
                profit_dont_buy = dp[i+1][0] if i < n-1 else 0
                
                # The maximum profit is the maximum of these two cases
                dp[i][0] = max(profit_buy, profit_dont_buy)
            
            # If a stock has been bought
            else:
                # Consider the case where we sell the stock
                # Add the price to the maximum profit that can be made from the remaining prices after selling
                profit_sell = price_list[i] + dp[i+1][0] if i < n-1 else 0
                
                # Consider the case where we don't sell the stock
                # The maximum profit is the maximum profit that can be made from the remaining prices without selling
                profit_dont_sell = dp[i+1][1] if i < n-1 else 0
                
                # The maximum profit is the maximum of these two cases
                dp[i][1] = max(profit_sell, profit_dont_sell)
    
    # Return the maximum profit that can be made from the first price
    return dp[0][0]

###