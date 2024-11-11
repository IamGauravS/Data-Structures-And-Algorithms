class Solution:
    def longestCommonSubsequences(self, text1: str, text2: str) -> list:
        len1, len2 = len(text1), len(text2)
        
        # Initialize a DP table where each cell stores a set of subsequences
        dp = [[set() for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        
        # Fill the DP table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # If characters match, add them to each subsequence from the previous diagonal cell
                if text1[i - 1] == text2[j - 1]:
                    if dp[i - 1][j - 1]:
                        dp[i][j] = {seq + text1[i - 1] for seq in dp[i - 1][j - 1]}
                    else:
                        dp[i][j].add(text1[i - 1])
                else:
                    # Otherwise, take the LCS set from top or left (whichever has longer subsequences)
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    elif len(dp[i - 1][j]) < len(dp[i][j - 1]):
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j].union(dp[i][j - 1])


        # The cell dp[len1][len2] contains all longest common subsequences
        max_length = max(len(seq) for seq in dp[len1][len2])
        longest_common_subsequences = sorted(seq for seq in dp[len1][len2] if len(seq) == max_length)
        result = sorted(dp[len1][len2])
        return result

# Example usage:
solution = Solution()
print(solution.longestCommonSubsequences("abcde", "ace"))
