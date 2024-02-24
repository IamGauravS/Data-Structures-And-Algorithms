## we can do at most 2 transactions

def when_to_buy_sell_two_transc(price_list, buy_sell_flag, no_of_transaction, index):
    if index == n:
        return 0
    if no_of_transaction == 2:
        return 0 
    if buy_sell_flag == False:
        when_buy = -price_list[index] + when_to_buy_sell_two_transc(price_list, True, no_of_transaction, index+1)
        when_not_buy = when_to_buy_sell_two_transc(price_list, False, no_of_transaction, index+1)
        return max(when_buy, when_not_buy)
    else:
        when_sell = price_list[index] + when_to_buy_sell_two_transc(price_list, False,no_of_transaction+1, index+1)
        when_not_sell = when_to_buy_sell_two_transc(price_list, buy_sell_flag, no_of_transaction, index+1)
        return max(when_sell, when_not_sell)
    


#This function uses a dynamic programming approach to find the maximum profit that can be made by buying and selling stocks with at most two transactions. It creates a dp table where dp[i][t][0] represents the maximum profit that can be made from the i-th price onwards if a stock hasn't been bought yet and t transactions have been made so far, and dp[i][t][1] represents the maximum profit that can be made from the i-th price onwards if a stock has been bought and t transactions have been made so far. It fills this table in a bottom-up manner, considering each price from the last to the first, and for each price, it considers two possibilities: buying or not buying if a stock hasn't been bought yet, and selling or not selling if a stock has been bought. The maximum profit that can be made from the first price with 0 transactions made so far is dp[0][2][0].

def when_to_buy_sell_two_transc(price_list):
    n = len(price_list)
    
    # Initialize the dp table
    dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n+1)]
    
    # Fill the dp table
    for i in range(n-1, -1, -1):
        for t in range(2, -1, -1):
            for flag in range(2):
                # If a stock hasn't been bought yet
                if flag == 0:
                    # Consider the case where we buy the stock
                    profit_buy = -price_list[i] + dp[i+1][t][1] if i < n-1 else 0
                    
                    # Consider the case where we don't buy the stock
                    profit_dont_buy = dp[i+1][t][0] if i < n-1 else 0
                    
                    # The maximum profit is the maximum of these two cases
                    dp[i][t][0] = max(profit_buy, profit_dont_buy)
                
                # If a stock has been bought
                else:
                    # Consider the case where we sell the stock
                    profit_sell = price_list[i] + dp[i+1][t-1][0] if i < n-1 and t > 0 else 0
                    
                    # Consider the case where we don't sell the stock
                    profit_dont_sell = dp[i+1][t][1] if i < n-1 else 0
                    
                    # The maximum profit is the maximum of these two cases
                    dp[i][t][1] = max(profit_sell, profit_dont_sell)
    
    # Return the maximum profit that can be made from the first price with 0 transactions made so far
    return dp[0][2][0]   