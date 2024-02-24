def knapsack_01(values, weights, capacity):
    n = len(values)
    # Initialize a table to store the maximum values for subproblems
    # dp[i][w] will store the maximum value that can be obtained using the first i items and a maximum weight of w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table dp in bottom-up manner
    for i in range(1, n + 1):  # Iterate over items
        for w in range(1, capacity + 1):  # Iterate over all possible weights
            # If the weight of the current item is less than or equal to the current weight w
            if weights[i - 1] <= w:
                # Update dp[i][w] to be the maximum of two cases:
                # 1) including the current item (which adds its value and subtracts its weight from the current weight w)
                # 2) not including the current item (which is the same as the maximum value for the previous items and the current weight w)
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the weight of the current item is greater than the current weight w
                # Just take the maximum value obtained without including the current item
                dp[i][w] = dp[i - 1][w]

    # Trace back in the dp table to find which items were selected to get the maximum value
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):  # Iterate over items in reverse order
        # If the maximum value with the current item i and weight w is different from the maximum value without the current item
        if dp[i][w] != dp[i - 1][w]:
            # It means the current item was selected, so add it to the list of selected items
            selected_items.append(i - 1)
            # Subtract the weight of the current item from the remaining weight
            w -= weights[i - 1]

    # Reverse the list of selected items to get them in the original order
    selected_items.reverse()
    # Return the maximum value and the list of selected items
    return dp[n][capacity], selected_items