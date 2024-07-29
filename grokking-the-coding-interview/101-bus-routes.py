import sys

def minimum_buses(bus_routes, src, dest):

    # Replace this placeholder return statement with your code
    edges = []
    bus_route_dict = {}
    
    for bus_route in bus_routes:
        
        
        if len(bus_route) > 1:
            for i in range(len(bus_route)-1):
               edges.append([bus_route[i], bus_route[i+1], 1])
            edges.append([bus_route[-1], bus_route[0], 1])
                
    for index, bus_route in enumerate(bus_routes):
        for bus in bus_route:
            bus_route_dict[bus] = index
    
    dist = {}
    pred = {}
    
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a not in dist:
            dist[a] = sys.maxsize
            pred[a] = None 
        if b not in dist:
            dist[b] = sys.maxsize
            pred[b] = None 
            
    dist[src] = 0 
    pred[src] = None 
            
    for _ in range(len(dist)-1): ## n-1 times
        for u, v, wt in edges:
            if dist[u] != sys.maxsize and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt 
                pred[v] = u 
                
    curr= dest
    path = []
    
    while curr != None:
        path.append(curr)
        curr = pred[curr]
        
    if path[-1] != src:
        return -1 
    
    path.reverse()
    bus_set = set()
    
    for p in path:
        route = bus_route_dict[p]
        bus_set.add(route)
        
    
    return len(bus_set)
        
    
                
    
        
            