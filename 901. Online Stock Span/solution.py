class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []
        self.count = 0

    def next(self, price: int) -> int:
        i = self.count
        while self.monotonic_stack and price >= self.monotonic_stack[-1][0]:
            _, i = self.monotonic_stack.pop()
        
        self.count += 1
        self.monotonic_stack.append((price, i))
        return (self.count - self.monotonic_stack[-1][1])


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.monotonic_stack and price >= self.monotonic_stack[-1][0]:
            _, sub_count = self.monotonic_stack.pop()
            count += sub_count
        
        self.monotonic_stack.append((price, count))
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)