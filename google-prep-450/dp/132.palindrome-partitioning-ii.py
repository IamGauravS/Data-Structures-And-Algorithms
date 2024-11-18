#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def checkIfAlreadyPalindrome(self, inputStr):
        start = 0
        end = len(inputStr) - 1

        while start < end:
            if inputStr[start] != inputStr[end]:
                return False
            start += 1
            end -= 1

        return True

    def minCutHelper(self, start, end):
        if start >= end or self.checkIfAlreadyPalindrome(self.s[start:end + 1]):
            return 0

        if (start, end) in self.dp:
            return self.dp[(start, end)]

        minPartition = float('inf')
        for ind in range(start, end):
            if self.checkIfAlreadyPalindrome(self.s[start:ind + 1]):
                noOfWays = 1 + self.minCutHelper(ind + 1, end)
                minPartition = min(noOfWays, minPartition)

        self.dp[(start, end)] = minPartition
        return self.dp[(start, end)]

    def minCutDP(self, s: str) -> int:
        self.s = s
        self.dp = {}
        return self.minCutHelper(0, len(s) - 1)
    
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Initialize the palindrome DP table
        is_palindrome = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            is_palindrome[i][i] = True

        # Fill the palindrome DP table
        for length in range(2, n + 1):  # length of the substring
            for start in range(n - length + 1):
                end = start + length - 1
                if s[start] == s[end]:
                    if length == 2:
                        is_palindrome[start][end] = True
                    else:
                        is_palindrome[start][end] = is_palindrome[start + 1][end - 1]

        # Initialize the cuts DP array
        cuts = [float('inf')] * n

        for i in range(n):
            if is_palindrome[0][i]:
                cuts[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        cuts[i] = min(cuts[i], cuts[j] + 1)

        return cuts[-1]

        
# @lc code=end

