class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        results = [[1]]

        while len(results) < numRows:
            currLevel = []
            numElements = len(results[-1]) + 1

            for i in range(numElements):
                if i == 0 or i == numElements-1:
                    currLevel.append(1)
                else:
                    currLevel.append(results[-1][i-1] + results[-1][i])

            results.append(currLevel)

        return results

                