def jump_game(nums):
    # Replace this placeholder return statement with your code
    stack = [0]
    visited = [False for i in range(len(nums))]
    while stack:
        curr_index = stack.pop()
        
        if visited[curr_index] == True:
            continue
        visited[curr_index] = True 
        
        no_of_jumps = nums[curr_index]
        for i in range(1, no_of_jumps+1):
            if curr_index + i == len(nums) -1:
                return True 
            if curr_index + i < len(nums):
                stack.append(curr_index+i)
                
                
    return False


## optimised greedy approach
def jump_game(nums):
    furthest_reach = 0
    for i in range(len(nums)):
        if i > furthest_reach:
            return False
        furthest_reach = max(furthest_reach, i + nums[i])
    return True
