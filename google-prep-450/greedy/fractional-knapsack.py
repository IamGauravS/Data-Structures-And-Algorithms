class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, values, weights, w):
        # Create a list of tuples (value-to-weight ratio, value, weight)
        weightsByValue = []
        for v, weight in zip(values, weights):
            weightsByValue.append((v / weight, v, weight))

        # Sort the items by value-to-weight ratio in descending order
        weightsByValue = sorted(weightsByValue, reverse=True, key=lambda x: x[0])

        maxValue = 0
        totalWeight = 0

        for density, value, weight in weightsByValue:
            if totalWeight + weight <= w:
                maxValue += value
                totalWeight += weight
            else:
                remainingWeight = w - totalWeight
                maxValue += density * remainingWeight
                break

        return maxValue

