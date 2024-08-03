class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ## step 1 : transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        ## step 2: reverse the matrix
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        return 