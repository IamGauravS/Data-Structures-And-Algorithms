class Solution:
    def maximumPoints(self, arr, n):
        # Edge case: if there's only one day, return the max points on that day
        if n == 1:
            return max(arr[0])
        
        # Initialize previous day points
        prev1, prev2, prev3 = arr[0][0], arr[0][1], arr[0][2]

        for i in range(1, n):
            # Calculate the maximum points for each task today
            curr1 = arr[i][0] + max(prev2, prev3)  # Task 0 on current day
            curr2 = arr[i][1] + max(prev1, prev3)  # Task 1 on current day
            curr3 = arr[i][2] + max(prev1, prev2)  # Task 2 on current day

            # Update previous day's points for the next iteration
            prev1, prev2, prev3 = curr1, curr2, curr3

        # Return the maximum points possible on the last day
        return max(prev1, prev2, prev3)