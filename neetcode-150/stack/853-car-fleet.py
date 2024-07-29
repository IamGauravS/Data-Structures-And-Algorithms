class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_position_speed = []
        for p, s in zip(position, speed):
            destination_time = (target - p)/s
            car_position_speed.append([p,destination_time])
            
        car_position_speed = sorted(car_position_speed, reverse=True)
        
        no_of_fleet = len(position)
        stack = []
        stack.append(car_position_speed[0][1])
        for i in range(1, len(car_position_speed)):
            if car_position_speed[i][1] <= stack[-1]:
                no_of_fleet-=1
            else:
                stack.append(car_position_speed[i][1]) 
                
                
        return no_of_fleet
        
        
        
        
        
## optimised version

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_position_speed = sorted([(p, (target - p) / s) for p, s in zip(position, speed)], reverse=True)
        
        no_of_fleet = len(position)
        stack = [car_position_speed[0][1]]
        for p, t in car_position_speed[1:]:
            if t <= stack[-1]:
                no_of_fleet -= 1
            else:
                stack.append(t)
        
        return no_of_fleet
    
    
## memory optimised

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_position_speed = sorted([(p, (target - p) / s) for p, s in zip(position, speed)], reverse=True)
        
        no_of_fleet = len(position)
        max_time = car_position_speed[0][1]
        for p, t in car_position_speed[1:]:
            if t <= max_time:
                no_of_fleet -= 1
            else:
                max_time = t
        
        return no_of_fleet