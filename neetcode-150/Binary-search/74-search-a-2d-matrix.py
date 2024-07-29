class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncolumns = len(matrix[0])
        
        end = nrows*ncolumns -1
        start = 0 
        
        
        while start <= end:
            mid = (start+end) //2
            curri = mid // ncolumns 
            currj = mid % ncolumns
            
            if matrix[curri][currj] == target:
                return True 
            elif matrix[curri][currj] < target:
                start = mid + 1 
                
            else:
                end = mid -1
                
        return False 
             
        
        
        
        