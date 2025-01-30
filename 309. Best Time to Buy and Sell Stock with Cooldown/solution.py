class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        s0 = [0] * n
        s1 = [0] * n
        s2 = [0] * n
        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = float("-inf")
        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1]) # rest at s0 or rest from s2
            s1[i] = max(s1[i-1], s0[i-1]-prices[i]) # rest at s1 or buy from s0
            s2[i] = s1[i-1] + prices[i] # sell from s1
        
        return max(s0[n-1], s2[n-1])

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/75928/share-my-dp-solution-by-state-machine-thinking