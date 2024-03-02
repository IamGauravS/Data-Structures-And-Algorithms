import heapq 

def maximum_capital(c, k, capitals, profits):

    ## map capital to profit and declare empty heap 
    capital_profit_map = {}
    heap = []

    ## push all the capital in heap 
    for i in range(len(capitals)):
        capital_profit_map[capitals[i]] = profits[i]
        heapq.heappush(heap, capitals[i])

    for i in range(k):
        temp_capitals = []
        profit = -1
        max_profit_capital = -1
        while heap:
            if heap[0] <= c:
               curr = heapq.heappop(heap)
               temp_capitals.append(curr)
               if capital_profit_map[curr]> profit:
                   profit = capital_profit_map[curr]
                   max_profit_capital = curr 

            else:
                break 

        c = c + profit 

        for capt in temp_capitals:
            if capt != max_profit_capital:
                heapq.heappush(heap, capt)


    return c
               
    
## optimised version

def maximum_capital(c, k, capitals, profits):
    # Create a list of (capital, profit) pairs and sort it by capital
    projects = sorted(zip(capitals, profits))

    # Initialize a max heap for profits
    heap = []

    # Index for the current project
    i = 0

    # Perform k operations
    for _ in range(k):
        # Push all projects that can be completed to the heap
        while i < len(projects) and projects[i][0] <= c:   ### this wont add duplicate value as we are also increasing i and we
            ## are adding new projects if they come 
            # Use negative profit to get a max heap
            heapq.heappush(heap, -projects[i][1])
            i += 1

        # If the heap is empty, no projects can be completed
        if not heap:
            break

        # Pop the project with the highest profit from the heap
        c -= heapq.heappop(heap)

    return c