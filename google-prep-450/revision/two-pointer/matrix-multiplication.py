class Solution:
    def matrixMultiplicationHelper(self, arr, start, end):
        if start + 1 == end:
            return 0

        if (start, end) in self.memDict:
            return self.memDict[(start, end)]

        minValue = float('inf')
        for ind in range(start + 1, end):
            cost = (
                arr[start] * arr[ind] * arr[end]
                + self.matrixMultiplicationHelper(arr, start, ind)
                + self.matrixMultiplicationHelper(arr, ind, end)
            )
            minValue = min(minValue, cost)

        self.memDict[(start, end)] = minValue
        return minValue

    def matrixMultiplication(self, arr):
        # Initialize memoization dictionary
        self.memDict = {}
        return self.matrixMultiplicationHelper(arr, 0, len(arr) - 1)