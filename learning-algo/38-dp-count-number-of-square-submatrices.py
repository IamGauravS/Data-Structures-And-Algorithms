## dp[i][j] means how many squares end at i,j basically right bottom we copy the first row and first column
## if right left and before are 1 then we take the miimal of all of them and add 1 to them bcoz if take anything else it will form a rectangle

def count_total_no_of_rect(arr):
    dp_array  = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]

    dp_array[0] = arr[0].copy()

    for i in range(len(arr)):
        dp_array[i][0] = arr[i][0]
    n = len(arr)
    
    # Filling the DP array
    for i in range(1, n):
        for j in range(1, n):
            # If the cell in the original matrix is 1, then this cell can be the bottom-right corner of a square submatrix
            if arr[i][j] == 1:
                # The size of the square submatrix is determined by the smallest square submatrix that includes the cells to the left, above, and diagonally above-left of the current cell
                dp_array[i][j] = 1 + min(dp_array[i-1][j], dp_array[i][j-1], dp_array[i-1][j-1])

    count = 0
    for i in range(n):
        for j in range(n):
            count += dp_array[i][j]

    return count 

    