class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinations = [0] * (amount + 1)
        combinations[0] = 1 # 0 amount can be made in 1 way by using no coins

        for coin in coins:
            for amt in range(coin, amount + 1):
                combinations[amt] += combinations[amt - coin]
        
        return combinations[amount]