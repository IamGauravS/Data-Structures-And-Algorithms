import heapq

def min_refuel_stops(target, start_fuel, stations):
    heap = []
    stations.append([target, 0])
    curr_fuel = start_fuel
    no_of_stops = 0
    i = 0

    while curr_fuel < target:
        while i < len(stations) and stations[i][0] <= curr_fuel:
            heapq.heappush(heap, -stations[i][1])
            i += 1
        if not heap:
            return -1
        curr_fuel += -heapq.heappop(heap)
        no_of_stops += 1

    return no_of_stops