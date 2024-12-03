class Solution:
    def all_longest_common_subsequences(self, s, t):
        # Initialize the DP table
        dp = [[set() for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

        # Base case: Empty subsequences
        for i in range(len(t) + 1):
            dp[i][0] = {""}
        for j in range(len(s) + 1):
            dp[0][j] = {""}

        # Fill the DP table
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:  # Characters match
                    for seq in dp[i - 1][j - 1]:
                        dp[i][j].add(seq + t[i - 1])
                else:  # Characters do not match
                    if len(next(iter(dp[i - 1][j]))) > len(next(iter(dp[i][j - 1]))):
                        dp[i][j] = dp[i - 1][j]
                    elif len(next(iter(dp[i - 1][j]))) < len(next(iter(dp[i][j - 1]))):
                        dp[i][j] = dp[i][j - 1]
                    else:  # Lengths are equal, take union
                        dp[i][j] = dp[i - 1][j].union(dp[i][j - 1])

        # Get all LCS from the last cell
        return sorted(dp[len(t)][len(s)])
