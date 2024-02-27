### given the n matrix dimensions tell me the minimum cost to multiply 

## arr[] = [10,20,230,40]  matrix dimenstions are [10,20], [20,230], [230,40]
## 1. start with entire block (represent them as i,j)
## 2. try to break into partition (AB)(CD) (A)(BCD) (ABC)(D) 
## 4.  i is the start point j is the end point 
## 5. try all partion (run a loop to try all partition)
## 6. return the best possible two partition
## 7. f(1,4) returns minimum multiplication to solve matrix from 1 to 4
import sys
def find_minimum_num_ops(arr, i,j):
    if i==j:
          return 0 ## if there is only single matrix
     ## run a loop from i to j-1 then partitions would be f(i,k) f(k+1,j) 
     ## we will only go to j-1 since we want something in the right
    ## we start with 1st index
    
    min_prt = sys.maxsize
    for k in range(i, j):
         no_of_op = arr[i-1] * arr[k] * arr[j] + find_minimum_num_ops(arr, i,k) + find_minimum_num_ops(arr, k+1,j)
         min_prt = min(min_prt, no_of_op)

    return min_prt



arr =  [10,20,30,40,50]        
n = len(arr)
dp = [[-1 for _ in range(n)] for _ in range(n)]
min_ops = find_minimum_num_ops(arr, 1, n-1, dp)


import sys

def find_minimum_num_ops(arr, i, j, dp):
    if i == j:
        return 0  # if there is only a single matrix

    # If this subproblem has already been solved, return the answer
    if dp[i][j] != -1:
        return dp[i][j]

    # Initialize the minimum operations to a large number
    min_prt = sys.maxsize

    # Try all possible partitions and update the minimum operations
    for k in range(i, j):
        no_of_op = arr[i-1] * arr[k] * arr[j] + find_minimum_num_ops(arr, i, k, dp) + find_minimum_num_ops(arr, k+1, j, dp)
        min_prt = min(min_prt, no_of_op)

    # Store the minimum operations for this subproblem in the DP table
    dp[i][j] = min_prt

    return min_prt