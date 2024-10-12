from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        charCount = defaultdict(int)

        for ch in s:
            charCount[ch] += 1


        sortedChars = sorted(charCount.items(), key=lambda item: item[1], reverse=True)

        result = ''.join(ch*freq for ch, freq in sortedChars)
        return result

