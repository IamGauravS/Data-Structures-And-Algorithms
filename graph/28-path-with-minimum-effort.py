

import sys
import heapq
def find_shortest_dist(matrix, src, dest):
    
    length = len(matrix)
    width = len(matrix[0])
    effort = [[sys.maxsize for i in range(width)] for j in range(length)]
    
    effort[src[0]][src[1]] = 0
    
    heap = []
    heapq.heappush(heap, (0, src))
    
    while heap:
        e, curr = heapq.heappop(heap)
        
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for dx, dy in delta:
            if 0 <= curr[0] +dx < length and 0 <= curr[1] + dy < width :
                effort_required = abs(matrix[curr[0]][curr[1]] - matrix[curr[0] +dx][curr[1] + dy])
                
                if effort[curr[0] +dx][curr[1] + dy] > e + effort_required:
                    effort[curr[0] +dx][curr[1] + dy] = e + effort_required
                    heapq.heappush(heap, (e + effort_required, (curr[0]+dx, curr[1]+dy)))
                    
                    
    return effort[dest[0]][dest[1]] if effort[dest[0]][dest[1]] != sys.maxsize else -1
    