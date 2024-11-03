#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        paths = []
        queue = deque()
        queue.append([beginWord])
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while queue:
            queueLen = len(queue)
            currWordSet = set()
            for _ in range(queueLen):
                currPath = queue.popleft()
                if currPath[-1] == endWord:
                    paths.append(currPath)
                    continue 
                for i in range(len(currPath[-1])):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = currPath[-1][:i] + c + currPath[-1][i+1:]
                        if newWord in wordSet:
                            queue.append(currPath + [newWord])
                            currWordSet.add(newWord)


            wordSet = wordSet - currWordSet

        return paths


# @lc code=end

## more optimised version

from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Initialize variables for bidirectional BFS
        forward_queue = deque([[beginWord]])
        backward_queue = deque([[endWord]])
        forward_visited = {beginWord: [[beginWord]]}
        backward_visited = {endWord: [[endWord]]}
        wordSet.discard(beginWord)
        wordSet.discard(endWord)
        found = False
        result = []

        def visit_word_node(queue, visited, other_visited):
            nonlocal found
            level_visited = defaultdict(list)
            for _ in range(len(queue)):
                path = queue.popleft()
                current_word = path[-1]
                for i in range(len(current_word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = current_word[:i] + c + current_word[i+1:]
                        if new_word in other_visited:
                            found = True
                            for other_path in other_visited[new_word]:
                                if visited is forward_visited:
                                    result.append(path + other_path[::-1])
                                else:
                                    result.append(other_path + path[::-1])
                        if new_word in wordSet and new_word not in visited:
                            level_visited[new_word].append(path + [new_word])
            queue.extend(level_visited[new_word] for new_word in level_visited)
            visited.update(level_visited)

        while forward_queue and backward_queue and not found:
            if len(forward_queue) <= len(backward_queue):
                visit_word_node(forward_queue, forward_visited, backward_visited)
            else:
                visit_word_node(backward_queue, backward_visited, forward_visited)

        return result

# Example usage
