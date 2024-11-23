#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # Step 1: Precompute the palindromic substrings
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True  # Single character is always a palindrome

        for length in range(2, n + 1):  # Check substrings of length >= 2
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:  # Two-character substrings
                        is_palindrome[i][j] = True
                    else:  # Longer substrings
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]

        # Step 2: Backtracking with DP
        def backtrack(start: int, path: List[str]):
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if is_palindrome[start][end]:  # Check if s[start:end+1] is a palindrome
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result

        
# @lc code=end

