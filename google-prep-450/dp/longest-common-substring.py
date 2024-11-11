class Solution:
    def longestCommonSubstr(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        
        # DP table to store the lengths of longest common suffixes of substrings
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        max_len = 0  # To keep track of the maximum length of common substring

        # Build the dp table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # If characters match, extend the substring length
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])  # Update max length
                else:
                    dp[i][j] = 0  # Reset if characters don't match

        return max_len


## print longest common substring
## keep track of end index
## longest common substring = s1[end_index - max_len:end_index]

class Solution:
    def longestCommonSubstr(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        
        # DP table to store the lengths of longest common suffixes of substrings
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        max_len = 0  # To keep track of the maximum length of common substring
        end_index = 0  # To store the ending index of the longest common substring in s1

        # Build the dp table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # If characters match, extend the substring length
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # Update max length and end index
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_index = i  # Update end index for s1
                else:
                    dp[i][j] = 0  # Reset if characters don't match

        # Extract the longest common substring from s1
        longest_common_substring = s1[end_index - max_len:end_index]
        return longest_common_substring
