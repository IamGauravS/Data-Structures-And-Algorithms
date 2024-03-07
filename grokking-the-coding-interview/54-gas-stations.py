def gas_station_journey(gas, cost):
    # Replace this placeholder return statement with your code
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    if total_gas < total_cost:
        return -1 
    
    
    for i in range(len(gas)):
        curr_gas = 0
        if gas[i] < cost[i]:
            continue
        else:
            j = 0
            curr_point = i
            prev_gas = 0
            while j < len(gas):
                curr_gas = prev_gas + gas[curr_point % len(gas)]
                if curr_gas - cost[curr_point % len(gas)] >= 0:
                    j = j+1
                    prev_gas = curr_gas - cost[curr_point % len(gas)]
                    curr_point = curr_point + 1
                else:
                    break
                
            if j == len(gas):
                return i
            
            
    return -1 
                
       
## optimised     
def gas_station_journey(gas, cost):
    total_gas = 0
    total_cost = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0

    if total_gas < total_cost:
        return -1
    else:
        return start