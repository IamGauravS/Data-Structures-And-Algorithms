# The function find_longest_common_sub calculates the length of the longest common subsequence (LCS) of two strings str1 and str2.
# It uses a dynamic programming approach where dp[i][j] stores the length of the LCS of str1[0..i-1] and str2[0..j-1].
# For each pair of characters in str1 and str2, it updates dp[i][j] based on whether the characters match or not.
# If the characters match, dp[i][j] is 1 plus the length of the LCS of the remaining strings (i.e., dp[i-1][j-1]).
# If the characters don't match, dp[i][j] is the maximum of the lengths of the LCS of two cases:
# - str1 without its current character and str2 (i.e., dp[i-1][j])
# - str1 and str2 without its current character (i.e., dp[i][j-1]).
def find_longest_common_sub(str1, str2):
    dp = [[0]*(len(str1)+1) for i in range(len(str2)+1)]

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[j][i] = 1 + dp[j-1][i-1]
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])

    return dp[len(str2)][len(str1)]

# The function find_shortest_common_superseq calculates the length of the shortest common supersequence (SCS) of two strings str1 and str2.
# The length of the SCS of two strings is the sum of the lengths of the two strings minus the length of their LCS.
# It first calculates the length of the LCS using the function find_longest_common_sub, and then uses it to calculate the length of the SCS.
def find_shortest_common_superseq(str1, str2):
    len_long_sommon_sub = find_longest_common_sub(str1, str2)
    return len(str1) + len(str2) - len_long_sommon_sub