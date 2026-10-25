# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from euler import solution
from typing import Tuple


@solution
def solve():
    months = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
    }
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    
    

    date = (1,1,1900)
    weekday = weekdays[0]

    def update_weekday():
        weekday_i = weekdays.index(weekday)
        weekdays_len = len(weekdays)
        if weekday_i == weekdays_len-1:
            return weekdays[0]
        else: 
            return weekdays[weekday_i+1]
        
    print(date, weekday)
    sunday_count = 0
    while date != (31,12,2000):
        
        day = date[0]
        month = date[1]
        year = date[2]
        #check year change
        if month == 12 and day == 31:
            date = (1,1,year+1)
            weekday = update_weekday()
            

        #check month change
        elif day >= months[month]:
            is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
            if is_leap and month == 2 and day == 28:
                date = (day+1,month,year)
                weekday = update_weekday()
            else:
                date = (1,month+1,year)
                weekday = update_weekday()
        
        else:
            date = (day+1,month,year)
            weekday = update_weekday()
            

        if date[2] > 1900 and weekday == weekdays[6] and date[0] == 1:
            sunday_count += 1
    return sunday_count
            

if __name__ == "__main__":
    solve()