def find_no_of_ways(chain_arr, value, index):
    if value ==0:
        return 1 
    if index == len(chain_arr)-1:
        if value % chain_arr[index] == 0:
            return 1
        else:
            return 0
    take = 0
    if value -chain_arr[index] >0:    
        take = find_no_of_ways(chain_arr, value-chain_arr[index], index)
    nottake = find_no_of_ways(chain_arr, value, index+1)

    return take + nottake


def find_no_of_ways(chain_arr, value, index, dp):
    # If the value is 0, we have found a way to make up the value, so return 1
    if value == 0:
        return 1

    # If the value is negative, it means we have overshot the value, so this way is not valid, return 0
    if value < 0:
        return 0

    # If we have used all coins and the value is still not 0, it means we can't make up the value with these coins, return 0
    if index == len(chain_arr):
        return 0

    # If this subproblem has already been computed, return the stored result
    if dp[index][value] != -1:
        return dp[index][value]

    # Compute the result for this subproblem
    # Consider two cases: taking the current coin and not taking the current coin
    # If we take the current coin, subtract its value from the total value
    # If we don't take the current coin, move to the next coin
    take = find_no_of_ways(chain_arr, value - chain_arr[index], index, dp)
    nottake = find_no_of_ways(chain_arr, value, index + 1, dp)

    # Store the result in the dp table
    # The result is the sum of the number of ways when taking the current coin and when not taking it
    dp[index][value] = take + nottake

    return dp[index][value]

# Example usage:
chain_arr = [1, 2, 3]  # The available coins
value = 4  # The value to make up
# Initialize a dp table with -1
# dp[i][j] will store the number of ways to make up a value j using the first i coins
dp = [[-1 for _ in range(value + 1)] for _ in range(len(chain_arr))]
# Call the function and print the result
print(find_no_of_ways(chain_arr, value, 0, dp))  # Output: 4

# Example usage:
chain_arr = [1, 2, 3]
value = 4
dp = [[-1 for _ in range(value + 1)] for _ in range(len(chain_arr))]
print(find_no_of_ways(chain_arr, value, 0, dp))  # Output: 4