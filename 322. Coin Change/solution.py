class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n_coins, remainder = 0, 0
        min_change = [0] * (amount + 1)
        coins.sort()
        
        for curr_amount in range(1, amount+1):
            min_coins = float("inf")
            for coin in coins:
                if coin > curr_amount:
                    break
                min_coins = min(min_coins, min_change[curr_amount - coin] + 1)

            min_change[curr_amount] = min_coins
        
        if min_change[-1] == float("inf"):
            return -1
        
        return min_change[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_change = [amount+1] * (amount + 1)
        min_change[0] = 0
        coins.sort()
        
        for curr_amount in range(1, amount+1):
            for coin in coins:
                if coin > curr_amount:
                    break
                min_change[curr_amount] = min(min_change[curr_amount], min_change[curr_amount - coin] + 1)        
        if min_change[-1] == amount+1:
            return -1
        
        return min_change[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_change = [amount+1] * (amount + 1)
        min_change[0] = 0

        for coin in coins:
            for curr_amount in range(coin, amount+1):
                min_change[curr_amount] = min(min_change[curr_amount], min_change[curr_amount - coin] + 1)
        if min_change[-1] == amount+1:
            return -1
        
        return min_change[-1]