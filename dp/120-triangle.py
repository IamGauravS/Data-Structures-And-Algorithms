class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangleHeight = len(triangle)

        dp = [[float('inf')]* triangleHeight for i in range(triangleHeight)]

        dp[0][0] = triangle[0][0]

        for i in range(1, triangleHeight):
            dp[i][0] = triangle[i][0] + dp[i-1][0]

        for i in range(1, triangleHeight):
            for j in range(1, len(triangle[i])):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]


        return min(dp[-1])