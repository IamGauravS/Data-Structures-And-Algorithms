
import sys
def dfs(nums, start, end, target,  no_of_multiplication, visited, no_of_multiplication_till_now):
    if start > target:
        return 
    
    if start == target:
        if no_of_multiplication_till_now < no_of_multiplication[0]:
            no_of_multiplication[0] = no_of_multiplication_till_now
        return 
    
    if visited[start] == True:
        return
    
    visited[start] = True 
    
    no_of_multiplication_till_now +=1
    
    for num in nums:
        dfs(nums, start*num * 100000, end, target,  no_of_multiplication, visited, no_of_multiplication_till_now)
        
    no_of_multiplication_till_now -=1
    visited[start] = False 
        
    return 
    


def minimum_multiplication(nums, start, end, target):
    no_of_multiplication = [sys.maxsize]
    no_of_multiplication_till_now = 0
    visited = {i: False for i in range(start, target+1)}
    dfs(nums, start, end, target,  no_of_multiplication, visited, no_of_multiplication_till_now)
    
    return no_of_multiplication[0]


## optimised way
import sys

def minimum_multiplication(nums, start, target):
    dp = [sys.maxsize] * (target + 1)
    dp[start] = 0

    for num in nums:
        for i in range(num, target + 1):
            if i % num == 0:
                dp[i] = min(dp[i], dp[i // num] + 1)

    return dp[target] if dp[target] != sys.maxsize else -1



import heapq

def minimum_multiplication(nums, start, target):
    heap = [(0, start)]  # (number of multiplications, current number)
    visited = {start: 0}  # keep track of the minimum number of multiplications for each number

    while heap:
        no_of_multiplication, num = heapq.heappop(heap)

        if num == target:
            return no_of_multiplication

        for next_num in nums:
            new_num = num * next_num

            if new_num > target:
                continue

            new_no_of_multiplication = no_of_multiplication + 1

            if new_num not in visited or new_no_of_multiplication < visited[new_num]:
                visited[new_num] = new_no_of_multiplication
                heapq.heappush(heap, (new_no_of_multiplication, new_num))

    return -1