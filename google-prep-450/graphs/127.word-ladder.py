#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
class Solution:
    def is_one_char_diff(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        diff_count = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                diff_count += 1
            if diff_count > 1:
                return False
        
        return diff_count == 1


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)

        queue = deque()
        parent = {}
        parent[beginWord] = None 
        queue.append(beginWord)

        while queue:
            currWord = queue.popleft()

            for word in wordList:
                if word not in parent and self.is_one_char_diff(currWord, word):
                    parent[word] = currWord
                    queue.append(word)
                    if word == endWord:
                        break 

        transformationSequence  = []
        curr = endWord
        while curr:
            transformationSequence.append(curr)
            if curr in parent:
                curr = parent[curr]
            else:
                return 0

        if transformationSequence[-1] == beginWord:
            return len(transformationSequence)
        else:
            return 0


        
# @lc code=end

## optimised version

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        queue = deque([beginWord])
        length = 1  # Start with the first word

        while queue:
            for _ in range(len(queue)):
                currWord = queue.popleft()

                if currWord == endWord:
                    return length  # Found the end word, return the length

                # Generate all possible transformations
                for i in range(len(currWord)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = currWord[:i] + char + currWord[i+1:]
                        if newWord in wordSet:
                            queue.append(newWord)
                            wordSet.remove(newWord)  # Remove to prevent re-visiting

            length += 1  # Increment the length for each level in BFS

        return 0  # If we finish and did not find the end word
