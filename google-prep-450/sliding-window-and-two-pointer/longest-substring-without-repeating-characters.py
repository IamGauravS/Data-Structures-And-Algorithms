class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenLongestSubStr = 0
        start = 0
        end = 0
        uniqueCharSet = set()

        while end < len(s):  # Only move 'end' within bounds
            if s[end] not in uniqueCharSet:
                uniqueCharSet.add(s[end])
                end += 1
                lenLongestSubStr = max(lenLongestSubStr, end - start)
            else:
                # Remove characters starting from 'start' until we remove the duplicate
                uniqueCharSet.remove(s[start])
                start += 1

        return lenLongestSubStr


## slightly optimised

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenLongestSubStr = 0
        start = 0
        uniqueCharSet = set()

        for end in range(len(s)):  # Use `for` loop to manage `end` increment
            while s[end] in uniqueCharSet:  # If a duplicate is found
                uniqueCharSet.remove(s[start])  # Remove from set
                start += 1  # Move the `start` pointer to the right
            
            uniqueCharSet.add(s[end])  # Add the current character to the set
            lenLongestSubStr = max(lenLongestSubStr, end - start + 1)  # Update the longest length

        return lenLongestSubStr
