class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        res = self.i - self.stack[-1][1] if self.stack else (self.i + 1)
        self.stack.append([price, self.i])
        self.i+=1
        return res