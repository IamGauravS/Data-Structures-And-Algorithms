class TicTacToe:
    # Constructor will be used to initialize TicTacToe data members 
    def __init__(self, n): 
        
        # Write your code here
        self.row_count = [0]*n 
        self.column_count = [0]*n 
        self.diagonal1 = 0
        self.diagonal2 = 0  
        self.size = n    

    # move will be used to play a move by a specific player and identify who
    # wins at each move
    def check_if_winner(self):
        if self.size in self.row_count or self.size in self.column_count or self.diagonal1 == self.size or self.diagonal2 == self.size:
            return 1
        if -self.size in self.row_count or -self.size in self.column_count or self.diagonal1 == -self.size or self.diagonal2 == -self.size:
            return 2
        return 0
    
    def move(self, row, col, player):
        
        # Replace this placeholder return statement with your code
        if player ==1:
            self.row_count[row] += 1
            self.column_count[col] +=1
            
            if row == col:
                self.diagonal1 += 1
            elif row + col == self.size-1 :
                self.diagonal2 += 1
        
        if player ==2:
            self.row_count[row] -= 1
            self.column_count[col] -=1
            
            if row == col:
                self.diagonal1 -= 1
            elif row + col == self.size-1 :
                self.diagonal2 -= 1
                
        return self.check_if_winner()
                 
            
             
         
        
