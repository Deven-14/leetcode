class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")
        year, month, day = int(year), int(month), int(day)
        month_to_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            month_to_days[2] += 1
        
        return sum(month_to_days[:month]) + day