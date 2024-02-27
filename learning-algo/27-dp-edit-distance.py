# The function find_edit_distance calculates the minimum number of operations (insertions, deletions, and replacements)
# required to transform str1 into str2. It uses a recursive approach, which can lead to recalculations of the same subproblems.

def find_edit_distance(str1, str2, i, j):   
    # If str1 is empty, all characters of str2 need to be inserted
    if i<0:
        return j+1
    # If str2 is empty, all characters of str1 need to be deleted
    if j<0:
        return i+1
    
    # If last characters are same, ignore last character and recur for remaining string
    if str1[i] == str2[j]:
        return 0 + find_edit_distance(str1, str2, i-1, j-1)
    
    # If last character are different, consider all possibilities and find minimum
    insert_op = 1 + find_edit_distance(str1, str2, i, j-1)  # Insert
    replace_op = 1+ find_edit_distance(str1, str2, i-1, j-1)  # Replace
    delete_op = 1+ find_edit_distance(str1, str2, i-1, j)  # Delete

    return min(insert_op, replace_op, delete_op)


# The function find_edit_distance_memo is an optimized version of find_edit_distance. It uses a dynamic programming table dp
# to store the results of subproblems, which significantly improves its efficiency by avoiding recalculations.

def find_edit_distance_memo(str1, str2, i, j, dp):
    # If str1 is empty, all characters of str2 need to be inserted
    if i<0:
        return j+1
    # If str2 is empty, all characters of str1 need to be deleted
    if j<0:
        return i+1
    # If the result of this subproblem is already calculated, return it
    if dp[i][j] != -1:
        return dp[i][j]
    
    # If last characters are same, ignore last character and recur for remaining string
    if str1[i] == str2[j]:
        dp[i][j] = 0 + find_edit_distance_memo(str1, str2, i-1, j-1, dp)
        return dp[i][j]
    
    # If last character are different, consider all possibilities and find minimum
    insert_op = 1 + find_edit_distance_memo(str1, str2, i, j-1, dp)  # Insert
    replace_op = 1+ find_edit_distance_memo(str1, str2, i-1, j-1, dp)  # Replace
    delete_op = 1+ find_edit_distance_memo(str1, str2, i-1, j, dp)  # Delete

    dp[i][j] = min(insert_op, replace_op, delete_op)

    return dp[i][j]

"""
The approach to find the minimum edit distance between two strings str1 and str2 is to use dynamic programming. 

We initialize a 2D array dp where dp[i][j] represents the minimum edit distance between the first i characters of str1 and the first j characters of str2. 

The table is filled in a bottom-up manner. For each pair of characters in str1 and str2, we calculate the minimum cost of transforming the substring of str1 up to that character into the substring of str2 up to that character. 

If the current characters are the same, the cost is the same as the cost for the previous characters. If they are different, we consider three operations (insert, replace, and delete), perform each operation, and choose the one that leads to the minimum cost. 

The final result is the cost for the entire strings, which is stored in dp[len(str1)][len(str2)].
"""

def find_edit_distance_tabulation(str1, str2):
    # Initialize a 2D array (dp) with dimensions (len(str1)+1) x (len(str2)+1)
    dp = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    
    # If str1 is empty, all characters of str2 need to be inserted
    for j in range(len(str2)+1):
        dp[0][j] = j
    # If str2 is empty, all characters of str1 need to be deleted
    for i in range(len(str1)+1):
        dp[i][0] = i 

    # Iterate over each character in str1 and str2
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            # If the current characters of str1 and str2 are the same,
            # the cost is the same as the cost for the previous characters
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # If the current characters are different, consider all possibilities and find minimum
                insert_op = 1 + dp[i][j-1]  # Insert
                replace_op = 1 + dp[i-1][j-1]  # Replace
                delete_op = 1 + dp[i-1][j]  # Delete
                dp[i][j] = min(insert_op, replace_op, delete_op)

    # The minimum edit distance between str1 and str2 is stored in dp[len(str1)][len(str2)]
    return dp[len(str1)][len(str2)]