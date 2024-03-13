def container_with_most_water(height):
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        # Calculate the area
        h = min(height[left], height[right])
        w = right - left
        area = h * w

        # Update the maximum area
        max_water = max(max_water, area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water