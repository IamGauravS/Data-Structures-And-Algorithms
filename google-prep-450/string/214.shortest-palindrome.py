#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Create the combined string
        combined = s + "#" + s[::-1]
        
        # Compute the KMP table
        kmp_table = [0] * len(combined)
        j = 0
        
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = kmp_table[j - 1]
            if combined[i] == combined[j]:
                j += 1
            kmp_table[i] = j
        
        # The length of the longest palindromic prefix
        longest_palindromic_prefix_length = kmp_table[-1]
        
        # The characters to add to the beginning of the string
        to_add = s[longest_palindromic_prefix_length:][::-1]
        
        return to_add + s

# Example usage:

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return s 
        
        orgStr = s 
        reversedStr = s[::-1]

        maxPalindromi = -1
        orgKmp = 0
        reversedKmp = 0
        MOD = 10**9 + 7
        base = 29

        for i in range(len(orgStr)):
            orgCh = orgStr[i]
            orgKmp = (orgKmp*base + (ord(orgCh) - ord('a'))) % MOD 

            reversedCh = reversedStr[len(orgStr)-1-i]
            reversedKmp = (reversedKmp + (ord(reversedCh) - ord('a'))*(base ** i)) % MOD

            if orgKmp == reversedKmp:
                maxPalindromi = i 

        if maxPalindromi == len(orgStr) - 1:
            return s 

        prefixToAdd = s[maxPalindromi+1:][::-1]

        return prefixToAdd + orgStr 
        
        
# @lc code=end

