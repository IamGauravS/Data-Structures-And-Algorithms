class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid < 0:
                if not stack:
                    stack.append(asteroid)

                else:
                    while stack:
                        if stack[-1] < 0:
                            stack.append(asteroid)
                            break
                        elif stack[-1] == -asteroid:
                            stack.pop()
                            break 
                        elif stack[-1] < abs(asteroid):
                            stack.pop()
                            if not stack:
                                stack.append(asteroid)
                                break
                        else:
                            break

            else:
                stack.append(asteroid)

        return stack
                        
