class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        output_array = [[[0,0] for i in range(len(heights[0]))] for j in range(len(heights))]
        
        for i in range(len(heights)):
            output_array[i][0][0] = 1 
            output_array[i][len(heights[0])-1][1] = 1 
            
        for j in range(len(heights[0])):
            output_array[0][j][0] = 1 
            output_array[len(heights)-1][j][1] = 1 
            
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                curr_stack = set()
                self.dfs(heights, output_array, (i,j), curr_stack)
                
        output = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if output_array[i][j] == [1,1]:
                    output.append([i,j])
        return output
                
    def dfs(self, heights, output_array, src, curr_stack):
         i, j = src 
         
         if (i, j ) in curr_stack:
             return output_array[i][j]
         
         curr_stack.add((i,j))
         
         delta = [(0,1), (0,-1), (-1,0), (1,0)]
         maxp, maxa = output_array[i][j][0], output_array[i][j][1]
         for dx, dy in delta:
             newi = dx + i
             newj = dy + j
             
             if 0 <= newi < len(heights) and 0 <= newj < len(heights[0]) and  heights[i][j] >= heights[newi][newj]:
                 sp, sa = self.dfs(heights, output_array, (newi, newj), curr_stack)
                 if sp > maxp:
                     maxp = sp 
                 if sa > maxa:
                     maxa = sa 
                     
        
         output_array[i][j] = [maxp, maxa]

         return output_array[i][j][0], output_array[i][j][1]
        
         