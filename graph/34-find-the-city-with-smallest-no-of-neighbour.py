

import sys
def find_city_with_smallest_no_of_neghbours(edges, no_of_cities, cutoff_distance):
    
    distance = [[sys.maxsize for i in range(no_of_cities)] for j in range(no_of_cities)]
    
    for i in range(no_of_cities):
        distance[i][i] = 0 
        
    for edge in edges:
        src, dest, wt = edge 
        distance[src][dest] = wt 
        
        
    for k in range(no_of_cities):
        for i in range(no_of_cities):
            for j in range(no_of_cities):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                
    city_counts = {}
    
    for i in range(no_of_cities):
        city_counts[i] = 0
        for j in range(no_of_cities):
            if distance[i][j] < cutoff_distance:
                city_counts[i] +=1 
                
    sorted_city_counts = sorted(city_counts.items(), key = lambda item: item[1])
    
    return sorted_city_counts[0]