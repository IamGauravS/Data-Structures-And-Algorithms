def keep_track_of_min(price_list):
    # Initialize min_price to the first price in the list
    # This is the minimum price seen so far
    min_price = price_list[0]
    
    # Initialize profit to 0
    # This is the maximum profit that can be made
    profit = 0
    
    # Get the number of days
    n = len(price_list)
    
    # Iterate over the price list, starting from the second day
    for i in range(1, n):
        # Calculate the profit that could be made by buying at the minimum price and selling at the current price
        cost = price_list[i] - min_price 
        
        # Update the maximum profit if this profit is higher
        profit = max(profit, cost)
        
        # Update the minimum price if the current price is lower
        min_price = min(min_price, price_list[i])

    # Return the maximum profit
    return profit


###The logic behind this code is to keep track of the minimum price seen so far and the maximum profit that can be made. For each price, it calculates the profit that could be made by buying at the minimum price and selling at the current price, and updates the maximum profit if this profit is higher. It also updates the minimum price if the current price is lower. The maximum profit is returned at the end. This approach ensures that the maximum profit is found in a single pass through the price list, making it very efficient.