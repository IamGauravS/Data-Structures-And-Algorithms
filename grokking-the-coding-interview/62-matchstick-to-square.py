

def matchstick_to_square_helper(matchsticks, curr_length, side_length, curr_matchstick):
    if curr_matchstick == len(matchsticks):
        
        for length in curr_length:
            if length != side_length:
                return False
        return True 
    
    curr_matchstick_length = matchsticks[curr_matchstick]
    for i in range(4):
        if curr_length[i] + curr_matchstick_length <= side_length:
            curr_length[i] = curr_length[i] + curr_matchstick_length
            if matchstick_to_square_helper(matchsticks, curr_length, side_length, curr_matchstick+1) == True:
                return True
            
            curr_length[i] = curr_length[i] - curr_matchstick_length
            
    return False

def matchstick_to_square(matchsticks):

    # Replace this placeholder return statement with your code
    if len(matchsticks) < 4:
        return False 
    sum_matchstick = sum(matchsticks)
    if sum_matchstick % 4 != 0:
        return False 
    
    side_length = sum_matchstick/4 
    for match in matchsticks:
        if match > side_length:
            return False 
        
    curr_length = [0,0,0,0]
    matchsticks = sorted(matchsticks)
    
    return matchstick_to_square_helper(matchsticks, curr_length, side_length, 0)