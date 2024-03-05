def count_substrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                count += 1

    return count

###When we're checking if s[i:j] (substring from i to j) is a palindrome, we look at s[i+1:j-1] (substring from i+1 to j-1). If we start from the front, s[i+1:j-1] would not have been computed yet, so we wouldn't be able to use it to determine if s[i:j] is a palindrome.

##By starting from the back, we ensure that s[i+1:j-1] has already been computed when we're checking s[i:j], so we can use it to determine if s[i:j] is a palindrome. This is a common pattern in dynamic programming problems where the current result depends on previous results.