from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordCharMaps = {}
        visited = [0]*len(strs)
        for word in strs:
            wordCharMaps[word] = dict(Counter(word))
            

        groupedAnagram = []
        for i in range(len(strs)):
            if visited[i] == 0:
                temp = []
                temp.append(strs[i])
                visited[i] = 1
                for j in range(i+1, len(strs)):
                    if visited[j] == 0 and wordCharMaps[strs[i]] == wordCharMaps[strs[j]]:
                        temp.append(strs[j])
                        visited[j] = 1

                groupedAnagram.append(temp)
                

            

        return groupedAnagram
    


## optimised version

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in anagrams:
                anagrams[sortedWord] = []

            anagrams[sortedWord].append(word)

        return list(anagrams.values())