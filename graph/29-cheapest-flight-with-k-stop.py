
import sys 
import heapq
def cheapest_flight_with_k_stops(flights, no_of_stops, source, destination):
    
    ## src, dest, cost 
    adj_list = {}
    cost_list = {}
    for flight in flights:
        src, dest, cost = flight 
        
        if src not in adj_list:
            adj_list[src] = []
            
        adj_list[src]((dest, cost))
        cost_list[src] = sys.maxsize
        cost_list[dest] = sys.maxsize
        
        
    cost_list[source] = 0
    heap = []
    heapq.heappush(heap, (0, 0, source))
    
    while heap:
        cost, stops, curr = heapq.heappop(heap)
        
        for node, wt in adj_list[curr]:
            if cost_list[node] > cost + wt and stops + 1 <= no_of_stops:
                cost_list[node] = cost + wt 
                heapq.heappush(heap, (cost_list[node], stops+1, node))
                
                
    return cost_list[destination] if cost_list[destination] is not sys.maxsize else -1