class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brickBoundrySum = {}

        for row in wall:
            currBoundry = 0
            for brick in row[:-1]:  # Exclude the last brick in each row
                currBoundry += brick
                if currBoundry not in brickBoundrySum:
                    brickBoundrySum[currBoundry] = 0
                brickBoundrySum[currBoundry] += 1

        # If no boundaries are crossed, return the height of the wall
        if not brickBoundrySum:
            return len(wall)

        # The minimum number of bricks crossed is the height of the wall minus the maximum boundary count
        return len(wall) - max(brickBoundrySum.values())