#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def findFirstDiff(self, word1: str, word2: str) -> (str, str):
        # Find the first different character between word1 and word2
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                return char1, char2
        return '', ''

    def alienOrder(self, words: List[str]) -> str:
        # Initialize in-degrees and adjacency list for each unique character
        indegre = {char: 0 for word in words for char in word}
        adjList = defaultdict(list)
        
        # Build the graph edges based on the first difference between consecutive words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Check if word2 is a valid ordering after word1
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""  # Invalid order, return empty string
            
            char1, char2 = self.findFirstDiff(word1, word2)
            if char1 and char2:
                adjList[char1].append(char2)
                indegre[char2] += 1
        
        # Topological Sort (Kahn's Algorithm)
        queue = deque([ch for ch in indegre if indegre[ch] == 0])
        sortedCh = []
        
        while queue:
            currCh = queue.popleft()
            sortedCh.append(currCh)
            
            for neigh in adjList[currCh]:
                indegre[neigh] -= 1
                if indegre[neigh] == 0:
                    queue.append(neigh)
        
        # If sortedCh contains all characters, we found a valid order, otherwise there's a cycle
        if len(sortedCh) == len(indegre):
            return ''.join(sortedCh)
        else:
            return ""  # Cycle detected or invalid order


# @lc code=end

