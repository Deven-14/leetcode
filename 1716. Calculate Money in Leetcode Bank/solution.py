class Solution:
    def totalMoney(self, n: int) -> int:
        days = [0, 1, 3, 6, 10, 15, 21, 28]
        num_of_weeks, rem_days = divmod(n, 7)

        m = max(num_of_weeks - 1, 0)
        total_money = (num_of_weeks * 28) + ((m * (m + 1)) // 2) * 7
        total_money += days[rem_days] + rem_days * num_of_weeks

        return total_money