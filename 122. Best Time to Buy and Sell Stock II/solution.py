class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profits = [0] * n
        min_price = prices[0]
        price = prices[0]

        for i in range(n-1):
            for j in range(i+1, n):
                if prices[i] < prices[j]:
                    profits[j] = max(prices[j] - prices[i] + profits[i-1], profits[j])
                else:
                    profits[j] = max(profits[j-1], profits[j])

        return profits[n-1]


# ! TIMEOUT ON THE ABOVE SOLUTION, COVERT IT TO O(N)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/comments/1575662

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/comments/1576892 - 
# what is the meaning of this buying and selling on the same day, profit will be 0 right , so why they highligted in bold, if was selling and then buying on the same day then it would affect on the recurrence but this statement is just added for the sake.
# Am i wrong or it means something else , i solved assuming we cannot sell and then buy on the same day, we will buy on the next day .

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/comments/1570091
# Consider this input : [a, ......, b, ......., c....., d]. Where ... refers to some input in between. a&c are valleys and b&d are peaks.
# If point 3 is true then we can say that
# d-a > (b-a) + (d-c)
# i.e d > b+d-c but as b-c > 0
# i.e d > +ve + d

# which is a false. So we can always say that picking up immediate next peak will always yeild a better result.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit
    

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/comments/1956066/

# Take ex :- [1,4,7,8,6,4]
# if you take (1, 8) , diff = 7
# or if you take (1, 4), (4, 7), (7, 8), diff = 3 + 3 + 1 = 7

# Going directly to 8, or going to 8 by adding all differences in between is same in result, so rather than thinking to jump, think it in this way.