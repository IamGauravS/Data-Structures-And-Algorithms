#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = []

        for p, s in zip(position, speed):
            positionSpeed.append((p, s))

        positionSpeed.sort(reverse=True)

        i = 0
        stack = []

        while i < len(positionSpeed):

            p = positionSpeed[i][0]
            s = positionSpeed[i][1]

            timeToTargget = (target - p)/s

            if not stack:
                stack.append(timeToTargget)

            else:
                if timeToTargget > stack[-1]:
                    stack.append(timeToTargget)

            i += 1

                


        return len(stack)
                
                
# @lc code=end

