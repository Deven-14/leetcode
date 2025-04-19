class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        profits = [0] * n

        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[i] + fee < prices[j]:
                    profits[j] = max(profits[j], prices[j] - prices[i] - fee + profits[i - 1])
                else:
                    profits[j] = max(profits[j], profits[j - 1])
        
        return profits[n-1]


# time limit exceeded

# refer: 122. Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0

        for i in range(1, n):
            if prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
            elif prices[i] + fee < buy:
                buy = prices[i] + fee
        
        return profit