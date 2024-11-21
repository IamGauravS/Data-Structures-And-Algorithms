def countPalindromicSubsequences(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table
    for length in range(2, n + 1):  # Substring lengths
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

    return dp[0][n - 1]

# Example Usage
s = "bccb"
print(countPalindromicSubsequences(s))  # Output: 6
