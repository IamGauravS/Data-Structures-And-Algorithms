#
# @lc app=leetcode id=727 lang=python3
#
# [727] Minimum Window Subsequence
#

# @lc code=start
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        min_len = float('inf')
        start_index = -1

        i = 0  # Pointer for s1

        while i < m:
            # Forward pass: Match s2 in s1
            j = 0  # Pointer for s2
            while i < m and j < n:
                if s1[i] == s2[j]:
                    j += 1
                i += 1

            # If we did not match all of s2, break
            if j < n:
                break

            # Backward pass: Shrink the window
            end = i - 1  # End of the current window
            j = n - 1  # Pointer for s2
            while j >= 0:
                if s1[end] == s2[j]:
                    j -= 1
                end -= 1

            # Update the minimum window
            if i - end - 1 < min_len:
                min_len = i - end - 1
                start_index = end + 1

            # Move i to the next character after the start of the current window
            i = end + 2

        return "" if start_index == -1 else s1[start_index:start_index + min_len]

        
# @lc code=end

