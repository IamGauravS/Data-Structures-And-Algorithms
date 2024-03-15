

import sys
import heapq
def find_shortest_dist(matrix, src, dest):
    
    length = len(matrix)
    width = len(matrix[0])
    distance = [[sys.maxsize for i in range(width)] for j in range(length)]
    
    distance[src[0]][src[1]] = 0
    
    heap = []
    heapq.heappush(heap, (0, src))
    
    while heap:
        dest, curr = heapq.heappop(heap)
        
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for dx, dy in delta:
            if 0 <= curr[0] +dx < length and 0 <= curr[1] + dy < width and matrix[curr[0]+dx][curr[1]+dy] == 1:
                if distance[curr[0]+dx][curr[1]+dy] > dest + 1:
                    distance[curr[0]+dx][curr[1]+dy] = dest + 1 
                    heapq.heappush(heap, (dest+1, (curr[0] + dx, curr[1] + dy)))
                    
                    
    return distance[dest[0]][dest[1]] if distance[dest[0]][dest[1]] != sys.maxsize else -1
    