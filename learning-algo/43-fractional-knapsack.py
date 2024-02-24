def fractional_knapsack(values, weights, target):
    # Calculate the value/weight ratio for each item
    fractions = []
    for i in range(len(values)):
        fractions.append(values[i] / weights[i])

    # Create a list of tuples, each containing the weight, ratio, and value of an item
    items = []
    for i in range(len(values)):
        items.append((weights[i], fractions[i], values[i]))

    # Sort the items in descending order of ratio
    # This ensures that items with higher value-to-weight ratio are considered first
    items.sort(key=lambda x: x[1], reverse=True)

    # Initialize the total profit and the remaining weight
    profit = 0
    remaining_weight = target

    # Iterate over the items
    for item in items:
        # If the item's weight is less than or equal to the remaining weight, take the whole item
        if item[0] <= remaining_weight:
            profit += item[2]  # Add the value of the item to the total profit
            remaining_weight -= item[0]  # Subtract the weight of the item from the remaining weight
        # If the item's weight is more than the remaining weight, take a fraction of the item
        else:
            profit += remaining_weight * item[1]  # Add the value of the fraction of the item to the total profit
            break  # No more items can be taken after this

    # Return the total profit
    return profit