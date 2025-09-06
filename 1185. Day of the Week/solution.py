class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        total_days = (year - 1971) * 365
        leap_years = ((year-1) - 1968) // 4
        total_days += leap_years
        
        month_to_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            month_to_days[2] += 1
        
        day_of_year = 4 # instead of 0 because 1970 December 31th is a Thursday
        day_of_year += sum(month_to_days[:month]) + day
        total_days += day_of_year
        return day_of_week[total_days % 7]