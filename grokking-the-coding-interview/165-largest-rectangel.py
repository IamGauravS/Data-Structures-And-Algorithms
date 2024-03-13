def largest_rectangle(heights):
    heights.append(0)
    stack = [-1]
    max_area = 0

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()
    return max_area

## left smaller and right smaller guy 

## (right_smaller - left_smaller  + 1)* a[i]  ## brute force way 
 ## basically we can do two loops first for finding next smaller index and second for next greater index
 
 ## for finding next greater we can start from back 
 ## then for every i we have right smaller and left smaller and find area for each

