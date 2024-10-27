class StockSpanner:

    def __init__(self):
        self.stack = []
        self.size = 0

    def next(self, price: int) -> int:
        currPrice = price
        self.size = self.size + 1
        
        while self.stack and self.stack[-1][0] <= currPrice:
            self.stack.pop()

        if not self.stack:
            span = self.size
        else:
            span = self.size - self.stack[-1][1]

        self.stack.append((currPrice, self.size))
        return span 



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)