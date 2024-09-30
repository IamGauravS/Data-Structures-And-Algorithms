class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        noOfrows = len(matrix)
        noOfcols = len(matrix[0])

        row = 0
        col = noOfcols -1 

        while (row < noOfrows and col >= 0):
            if matrix[row][col] == target:
                return True 
            
            elif matrix[row][col] > target:
                col -= 1 

            else:
                row += 1


        return False

            
    