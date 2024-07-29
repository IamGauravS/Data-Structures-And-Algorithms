class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {ch:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                continue
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
                    
        visited = {}
        res = []
        
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True 
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True 
            visited[c] = False
            res.append(c)
            
        for c in adj:
            if dfs(c):
                return ""
            
        res.reverse()
        return "".join(res)
                
import queue
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = {ch:set() for w in words for ch in w}
        indegree = {ch:0 for w in words for ch in w}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    
                    adjList[w1[j]].add(w2[j])
                    break
                    
        for key in adjList:
            for neighbour in adjList[key]:
                indegree[neighbour] +=1
                
        topo = []
        charQueue = queue.Queue()
        for ch in indegree:
            if indegree[ch] == 0:
                charQueue.put(ch)
                
        while not charQueue.empty():
            currChar = charQueue.get()
            topo.append(currChar)
            
            for neighbour in adjList[currChar]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    charQueue.put(neighbour)
                    
        if len(topo) < len(indegree):
            ## means there is a cycle
            return ""
        else:
            return "".join(topo)
            
            
        
            