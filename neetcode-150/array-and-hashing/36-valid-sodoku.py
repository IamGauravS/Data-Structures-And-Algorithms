class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set_collection = [set() for i in range(9)]
        col_set_collection = [set() for i in range(9)]
        block_set_collection = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    block_i = i // 3
                    block_j = j // 3
                    block_n = block_i*3  + block_j
                    if board[i][j] not in row_set_collection[i] and board[i][j] not in col_set_collection[j] and board[i][j] not in block_set_collection[block_n]:
                        row_set_collection[i].add(board[i][j])
                        col_set_collection[j].add(board[i][j])
                        block_set_collection[block_n].add(board[i][j])
                    else:
                        return False 
                    
                    
        return True
                    
                    
                    
class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        col_set_collection = [set() for i in range(9)]
        block_set_collection = [set() for i in range(9)]
        
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    block_i = i // 3
                    block_j = j // 3
                    block_n = block_i*3  + block_j
                    if board[i][j] not in row_set and board[i][j] not in col_set_collection[j] and board[i][j] not in block_set_collection[block_n]:
                        row_set.add(board[i][j])
                        col_set_collection[j].add(board[i][j])
                        block_set_collection[block_n].add(board[i][j])
                    else:
                        return False 
                    
                    
        return True
                    
        
        
        
        