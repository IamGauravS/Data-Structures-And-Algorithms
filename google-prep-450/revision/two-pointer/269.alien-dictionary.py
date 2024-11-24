#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def firstCharDiff(self, word1, word2):
        min_length = min(len(word1), len(word2))
    
        for i in range(min_length):
            if word1[i] != word2[i]:
                return (word1[i], word2[i])
        
        return None
        
    def alienOrder(self, words: List[str]) -> str:
        adjList = defaultdict(list)
        indegre = {}
        all_chars = set()

        # Initialize indegree for all unique characters
        for word in words:
            for char in word:
                all_chars.add(char)
                if char not in indegre:
                    indegre[char] = 0

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            diffChars = self.firstCharDiff(word1, word2)
            if diffChars:
                adjList[diffChars[0]].append(diffChars[1])
                indegre[diffChars[1]] += 1
            elif len(word1) > len(word2):
                # If word1 is longer than word2 and no differing characters, it's invalid
                return ""

        queue = deque()
        for key, value in indegre.items():
            if value == 0:
                queue.append(key)

        topo = []

        while queue:
            currChar = queue.popleft()
            topo.append(currChar)

            for neighbor in adjList[currChar]:
                indegre[neighbor] -= 1
                if indegre[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo) == len(indegre):
            return "".join(topo)
        
        return ""
        
        
# @lc code=end

