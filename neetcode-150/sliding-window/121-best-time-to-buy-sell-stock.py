class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        min_value = prices[0]
        
        for i in range(1, len(prices)):
            if min_value < prices[i]:
                profit = prices[i] - min_value
                if profit > max_profit:
                    max_profit = profit
            else:
                min_value = prices[i]
                
        return max_profit
                    
            
        