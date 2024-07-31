import datetime

day = int(input("What day is it: "))
# date time does this automatically, however it crashes the program, and id rather do it a bit nicer.
if day > 31:
    print("Invalid day entered")
    exit(1)

month = int(input("What month is it: (in number form like 01 for jan)"))
# date time does this automatically, however it crashes the program, and id rather do it a bit nicer.
if month > 12:
    print("Invalid month entered")
    exit(1)
year = int(input("What year is it (in number form)"))

# uses the datetime module in order to put the date and time in the right form and then get the week day.
date = datetime.datetime(year, month, day)
weekday = date.weekday()
# Probably a better way to do this, however im trying not to use google as much as i can and this works.
if weekday == 0:
    weekdayword = "Monday"
elif weekday == 1:
    weekdayword = "Tuesday"
elif weekday == 2:
    weekdayword = "Wednesday"
elif weekday == 3:
    weekdayword = "Thursday"
elif weekday == 4:
    weekdayword = "Friday"
elif weekday == 5:
    weekdayword = "Saturday"
elif weekday == 6:
    weekdayword = "Sunday"

print("The day for the date", day, "/", month, "/", year, "is", weekdayword)