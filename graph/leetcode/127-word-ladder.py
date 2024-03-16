from collections import deque

class Solution:
    def get_variations(self, word):
        variations = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                variation = word[:i] + char + word[i+1:]
                variations.append(variation)
        return variations

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for variation in self.get_variations(word):
                if variation in wordSet:
                    queue.append((variation, length + 1))
                    wordSet.remove(variation)  # Ensure each word is only used once

        return 0