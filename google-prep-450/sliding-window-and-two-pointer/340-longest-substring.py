class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        end = 0
        lenLongestStr = 0
        uniqueCharacters = {}

        for end in range(len(s)):
            uniqueCharacters[s[end]] = uniqueCharacters.get(s[end], 0) + 1

            while len(uniqueCharacters) > k:
                uniqueCharacters[s[start]] -= 1
                if uniqueCharacters[s[start]] == 0:
                    del uniqueCharacters[s[start]]

                start += 1

            lenLongestStr = max(lenLongestStr, end - start + 1)


        return lenLongestStr

            