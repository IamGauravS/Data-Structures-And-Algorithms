from point import Point
import heapq


def euclidean_distance_2d(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5


def k_closest(points, k):
  
    # Replace this placeholder return statement with your code
    distance_heap = []
    origin = Point(0,0)
    
    for point in points:
        distance = euclidean_distance_2d(origin, point)
        heapq.heappush(distance_heap, [distance, point])
        
    output_list = []
    for i in range(k):
        curr = heapq.heappop(distance_heap)
        output_list.append(curr[1])
        
    return output_list