from graph import *
from collections import deque


def find_compilation_order(dependencies):

  # Replace this placeholder return statement with your code
  graph = {}
  indegree = {}
  
  for den in dependencies:
      parent = den[1]
      child = den[0]
      if parent not in graph:
          graph[parent] = [child]
      else:
          graph[parent].append(child)
          
      if parent not in indegree:
          indegree[parent] = 0
          
      if child not in indegree:
          indegree[child] = 0
          
  
  for node in graph:
      for child in graph[node]:
              indegree[child] +=1 
              
  q = deque()
  for node in indegree:
      if indegree[node] == 0:
          q.append(node)
          
  topo = []
  while q:
      curr = q.popleft()
      topo.append(curr)
      if curr in graph:   ### since we are removing curr from graph we need to reduce one indegree for all its children
        for child in graph[curr]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)
              
  return topo
            
      
      
  