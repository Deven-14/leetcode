from itertools import accumulate
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        
        max_prices = list(accumulate(reversed(prices), max))[::-1]
        max_profit = 0
        for i in range(n-1):
            max_profit = max(max_profit, max_prices[i+1]-prices[i])
        
        return max_profit

from itertools import accumulate
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price-min_price)
        
        return max_profit


from itertools import accumulate
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif (profit := price-min_price) > max_profit:
                max_profit = profit
        
        return max_profit
