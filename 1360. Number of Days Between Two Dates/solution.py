class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1
        
        y1, m1, d1 = (int(x) for x in date1.split("-"))
        y2, m2, d2 = (int(x) for x in date2.split("-"))

        if y1 == y2 and m1 == m2:
            return d2 - d1

        def is_leap_year(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if y1 == y2:
            if is_leap_year(y1):
                days_of_month[2] += 1

            days += days_of_month[m1] - d1
            days += sum(days_of_month[m1+1:m2])
            days += d2
            return days

        y = y1 + 1
        days = 0
        while y < y2:
            if is_leap_year(y):
                days += 366
            else:
                days += 365
            y += 1
        
        if is_leap_year(y1):
            days_of_month[2] += 1

        days += days_of_month[m1] - d1
        days += sum(days_of_month[m1+1:])
        
        if is_leap_year(y1):
            days_of_month[2] -= 1
        
        if is_leap_year(y2):
            days_of_month[2] += 1

        days += d2
        days += sum(days_of_month[:m2])
    
        return days
