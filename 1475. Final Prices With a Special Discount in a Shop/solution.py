class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices[:]

        for j in range(len(prices)):
            while stack and prices[j] <= prices[stack[-1]]:
                i = stack.pop()
                ans[i] = prices[i] - prices[j]
            stack.append(j)
        
        return ans