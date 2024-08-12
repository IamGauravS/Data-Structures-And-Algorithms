class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []
        
        numRows = len(matrix)
        numCols = len(matrix[0])

        left = 0 
        right = numCols - 1
        top = 0
        bottom = numRows -1

        spiralMatrix = []

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                spiralMatrix.append(matrix[top][i])

            top += 1

            for i in range(top, bottom+1):
                spiralMatrix.append(matrix[i][right])

            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    spiralMatrix.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    spiralMatrix.append(matrix[i][left])
                left += 1


        return spiralMatrix