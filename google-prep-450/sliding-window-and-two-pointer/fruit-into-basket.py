class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        maxFruits = 0
        fruit_count = {}

        for end in range(len(fruits)):
            fruit = fruits[end]
            if fruit in fruit_count:
                fruit_count[fruit] += 1
            else:
                fruit_count[fruit] = 1
            
            # If we have more than two types of fruits, shrink the window
            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1  # Shrink the window from the left
            
            # Update the maximum number of fruits collected
            maxFruits = max(maxFruits, end - start + 1)

        return maxFruits
