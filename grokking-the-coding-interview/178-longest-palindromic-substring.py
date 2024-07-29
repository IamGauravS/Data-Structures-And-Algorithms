def longest_palindromic_substring(s):
    if not s:
        return ""

    n = len(s)
    longest_length = 1
    start = 0
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > longest_length:
                        longest_length = length
                        start = i

    return s[start:start + longest_length]