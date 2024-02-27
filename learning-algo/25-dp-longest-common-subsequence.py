def longest_common_sub_re(str1, str2, index1, index2):
    if index1 < 0 or index2 < 0:
        return 0
    
    if str1[index1] == str2[index2]:
        return 1 + longest_common_sub_re(str1, str2, index1-1, index2-1)
    else:
        return 0 + max(longest_common_sub_re(str1, str2, index1-1, index2), longest_common_sub_re(str1, str2, index1, index2-1))
    



def longest_common_sub_dp(str1, str2, index1, index2, dp ):
    if index1 < 0 or index2 < 0:
        return 0
    
    if dp[index1][index2] != -1:
        return dp[index1][index2]
    
    if str1[index1] == str2[index2]:
        dp[index1][index2] = 1 + longest_common_sub_re(str1, str2, index1-1, index2-1)
        return dp[index1][index2]
    else:
        dp[index1][index2] =0 + max(longest_common_sub_re(str1, str2, index1-1, index2), longest_common_sub_re(str1, str2, index1, index2-1))
        return dp[index1][index2]
    


def longest_common_sub_tab(str1, str2):
    m = len(str1)
    n = len(str2)

    # Initialize a DP table with 0
    # dp[i][j] will store the LCS of str1[0..i-1] and str2[0..j-1]
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # Iterate over all characters in both strings
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If the current characters match, the LCS is 1 plus the LCS of the remaining strings
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            # If the current characters don't match, the LCS is the maximum of the LCS of two cases:
            # - The first string without its current character and the second string
            # - The first string and the second string without its current character
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    # Initialize an empty string to store the LCS
    lcs = [""] * length
    i = m
    j = n

    # Trace back from dp[m][n]
    while i > 0 and j > 0:
        # If the current characters match, they are part of the LCS
        if str1[i-1] == str2[j-1]:
            lcs[length-1] = str1[i-1]
            i -= 1
            j -= 1
            length -= 1
        # If not, move towards the direction of the larger value
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    # Print the LCS
    print("LCS:", "".join(lcs))



    