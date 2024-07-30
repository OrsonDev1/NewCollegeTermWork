import datetime

day = int(input("What day is it: "))
month = int(input("What month is it: (in number form like 01 for jan)"))
year = int(input("What year is it (in number form)"))

date = year, month, day
weekday = date.weekday()
print(weekday)