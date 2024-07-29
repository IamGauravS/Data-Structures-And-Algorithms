from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        sep = chr(257)  # Use a non-printable character as a separator
        encodedStr = ''
        for word in strs:
            encodedStr += word + sep + str(len(word)) + sep 
        return encodedStr

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        wordList = []
        sep = chr(257)
        i = 0
        while i < len(s):
            j = i
            while s[j] != sep:
                j += 1
            word = s[i:j]
            j += 1
            length = ''
            while s[j].isdigit():
                length += s[j]
                j += 1
            length = int(length)  # Convert the string length to an integer
            if length == len(word):
                wordList.append(word)
            i = j + 1
        return wordList

# Example usage
