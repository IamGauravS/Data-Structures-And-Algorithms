def find_duplicate(nums):
    # Phase 1: Using Floyd's Tortoise and Hare algorithm to find intersection point
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]  # Tortoise moves one step
        hare = nums[nums[hare]]  # Hare moves two steps
        if tortoise == hare:  # When they meet, it means we have found a cycle
            break

    # At this point, the tortoise has traveled distance 'd', and the hare has traveled '2d'.
    # They met inside the cycle, 'd' steps away from the start of the cycle.

    # Phase 2: Find the entrance to the cycle
    tortoise = nums[0]  # Reset the tortoise to the start
    while tortoise != hare:  # Keep moving until they meet again
        tortoise = nums[tortoise]  # Both tortoise and hare move one step at a time
        hare = nums[hare]

    # The point where they meet is the start of the cycle, which is the duplicate number.
    return hare


#The key insight of Floyd's algorithm is that the distance from the start of the array to the start of the cycle is the same as the distance from the point of intersection to the start of the cycle, when moving in the direction of the cycle. This is why we reset the tortoise to the start of the array and move both the hare and tortoise one step at a time. They will meet at the start of the cycle, which is the duplicate number.


## better explanation https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-find-the-duplicate-number