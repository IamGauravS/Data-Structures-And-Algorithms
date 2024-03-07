def rescue_boats(people, limit):
    
    # Replace this placeholder return statement with your code
    
    left = 0
    right = len(people) -1
    people = sorted(people) 
    no_of_boats = 0
    while left <= right:
        if people[right] + people[left] <= limit:
            no_of_boats+=1
            right -=1
            left +=1 
        else:
            no_of_boats +=1
            right -=1
            
    
    return no_of_boats