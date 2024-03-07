def two_city_scheduling(costs):
  # Replace this placeholder return statement with your code
  total_cost = 0
  diff = []
  for i in range(len(costs)):
      di = costs[i][0] - costs[i][1]
      diff.append([di, i])
      
  diff = sorted(diff)
  n = len(diff) //2
  for i in range(len(diff)):
      if i < n:
          
          total_cost = total_cost + costs[diff[i][1]][0]
      else:
          total_cost = total_cost + costs[diff[i][1]][1]
          
          
  return total_cost


### The idea behind this is that if the cost difference is large, inviting a person to a city with a lower cost is optimal, because the difference is large. After sorting the array based on difference, the costs with large differences will be in the second half of the array. When the difference is large, it means the second value will be much less than the first value in the costs array. Therefore, we are inviting the second half to City B for optimization