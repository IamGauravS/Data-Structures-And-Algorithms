# Import the sys module to get the maximum possible integer
#This function calculates the minimum cost for bursting balloons from index i to j. It uses a recursive approach to try all possible orders of bursting the balloons. For each order, it calculates the cost for bursting the mid balloon and adds the costs for bursting the remaining balloons on the left and right. It then returns the minimum cost among all orders. The cost for bursting a balloon i
import sys

# Define the function to calculate the minimum cost
def calculate_reward(arr, i, j):
    # If there are no balloons left, the cost is 0
    if i >= j:
        return 0 

    # Initialize the minimum cost to the maximum possible integer
    min_cost = sys.maxsize

    # Iterate over all possible positions for the last balloon to burst
    for mid in range(i, j):
        # Calculate the cost of bursting the mid balloon
        # The cost is the product of the numbers on the mid balloon and its two neighbors
        cost = arr[mid-1] * arr[mid] * arr[mid+1]

        # Add the cost of bursting the remaining balloons on the left and right
        # We make recursive calls to calculate these costs
        cost += calculate_reward(arr, i, mid-1) + calculate_reward(arr, mid+1, j)

        # Update the minimum cost if the current cost is smaller
        if cost < min_cost:
            min_cost = cost 

    # Return the minimum cost
    return min_cost

# The original array of balloon numbers
arr = [10,20,30,40,50]

# Create a new array with a 1 at the beginning and end
input_arr = [1]
for elem in arr:
    input_arr.append(elem)
input_arr.append(1)

# Call the function with the new array and print the result
# We start from the second element and end at the second last element
print(calculate_reward(input_arr, 1, len(input_arr)-1))

def calculate_reward(arr):
    n = len(arr)
    # Initialize dp array
    dp = [[0]*n for _ in range(n)]

    # Iterate over all possible lengths of subarrays
    for length in range(1, n+1):
        # Iterate over all possible starting points of subarrays
        for i in range(n-length+1):
            # Calculate the ending point of the subarray
            j = i + length - 1
            # Iterate over all possible last balloons to burst
            for k in range(i, j+1):
                # Calculate the number of coins from the left and right subarrays
                left = dp[i][k-1] if k != i else 0
                right = dp[k+1][j] if k != j else 0
                # Calculate the number of coins from bursting the last balloon
                last = arr[i-1]*arr[k]*arr[j+1] if i != 0 and j != n-1 else arr[k]
                # Update the dp value
                dp[i][j] = max(dp[i][j], left + right + last)

    # Return the maximum number of coins
    return dp[0][n-1]

arr = [10,20,30,40,50]
input_arr = [1]
for elem in arr:
    input_arr.append(elem)
input_arr.append(1)

print(calculate_reward(input_arr))