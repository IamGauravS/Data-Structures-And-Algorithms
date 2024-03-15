
import sys

def flowd_wershell(edges, no_of_nodes):
    
    distance = [[sys.maxsize for i in range(no_of_nodes)] for j in range(no_of_nodes)] 
    
    for i in range(no_of_nodes):
        for j in range(no_of_nodes):
            distance[i][j] = 0
            
    
    for edge in edges:
        src, dest, wt = edge
        
        distance[src][dest] = wt 
        
    
    for k in range(no_of_nodes):
        for i in range(no_of_nodes):
            for j in range(no_of_nodes):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][j] + distance[k][j]
                    
                    
    return distance