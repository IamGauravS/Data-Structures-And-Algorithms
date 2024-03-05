def longest_common_subsequence(str1, str2):

    # Replace this placeholder return statement with your code
    dp = [[0 for i in range(len(str1))] for j in range(len(str2))]
    
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            dp[0][i] = 1 
    for i in range(len(str2)):
        if str2[i] == str1[0]:
            dp[i][0] = 1
            
    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            if str2[i] == str1[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
                
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
                
    return dp[-1][-1]
                
    
    
    
