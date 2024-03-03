def jump_game_two(nums):
    # Replace this placeholder return statement with your code
    
    farthest_jump = 0
    current_jump = 0
    no_of_jumps = 0
    
    for i in range(len(nums)-1):
        farthest_jump = max(farthest_jump, i+nums[i])
        if i == current_jump:
            no_of_jumps+=1
            current_jump = farthest_jump
            
    return no_of_jumps