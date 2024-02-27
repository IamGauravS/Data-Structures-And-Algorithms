import sys

# Recursive function to solve the unbounded knapsack problem
def knapsackUtil(wt, val, ind, W, dp):
    # Base case: If there are no more items to consider (index is 0)
    # We can take as many of the first item as we can fit into the knapsack
    if ind == 0:
        return (W // wt[0]) * val[0]

    # If the result for this state is already calculated, return it
    # This is the memoization part, where we avoid redundant calculations
    if dp[ind][W] != -1:
        return dp[ind][W]

    # Calculate the maximum value when the current item is not taken
    # We simply move to the next item without taking the current one
    notTaken = knapsackUtil(wt, val, ind - 1, W, dp)

    # Initialize a variable to store the maximum value when the current item is taken
    taken = -sys.maxsize
    # If the current item can fit into the knapsack, consider taking it
    if wt[ind] <= W:
        # The value when taking the current item is its value plus the maximum value for the remaining weight
        taken = val[ind] + knapsackUtil(wt, val, ind, W - wt[ind], dp)

    # Store the maximum of "notTaken" and "taken" in the DP table
    # This is the maximum value we can get by considering the first "ind" items and a total weight of "W"
    dp[ind][W] = max(notTaken, taken)
    return dp[ind][W]

# Function to find the maximum value that can be obtained in unbounded knapsack
def unboundedKnapsack(n, W, val, wt):
    # Create a DP table initialized with -1
    # dp[i][j] will store the maximum value we can get by considering the first "i" items and a total weight of "j"
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
    return knapsackUtil(wt, val, n - 1, W, dp)

def main():
    wt = [2, 4, 6]  # The weights (lengths) of the rods
    val = [5, 11, 13]  # The values (prices) of the rods
    W = 10  # The total length of the rod to be cut
    n = len(wt)  # The number of different rods

    print("The Maximum value of items the thief can steal is", unboundedKnapsack(n, W, val, wt))

if __name__ == "__main__":
    main()