class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        output = [0 for i in range(len(temperatures))]
        stack = []
        stack.append(len(temperatures)-1)
        
        for i in range(len(temperatures)-2, -1, -1):
            
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                output[i] = stack[-1] - i 
            stack.append(i)
                
        return output
                    
                    
                
        
        