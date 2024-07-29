class Solution:
    def generateParenthesis_helper(self, n, output, open_count, close_count, curr):
        if open_count == n and close_count == n:
            output.append(curr)
            return 
        
        if open_count < n:
            self.generateParenthesis_helper(n, output, open_count+1, close_count, curr+"(")
        if close_count < open_count:
            self.generateParenthesis_helper(n, output, open_count, close_count+1, curr+")")
            
        return 
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        self.generateParenthesis_helper(n, output,0,0, "")
        
        return output