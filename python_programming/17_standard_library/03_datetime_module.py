# datetime module
import datetime  

# datetime.datetime.now() gives current local date & time
current = datetime.datetime.now()
print("Current date & time ->", current)


# datetime.date.today() gives only today's date
today = datetime.date.today()
print("Today's date ->", today)


# we can create our own date using year, month, day
custom_date = datetime.date(2026, 4, 13)
print("Custom date ->", custom_date)


# custom time creation
# time(hour, minute, second)
custom_time = datetime.time(14, 30, 45)
print("Custom time ->", custom_time)


# formatting date and time (important for exams)
# strftime() converts datetime into readable format
formatted = current.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date-time ->", formatted)
print(current.strftime("%H:%M:%S")) # formated time only
print(current.strftime("%d:%m:%y")) # formated date only



# extracting parts of date/time
print("Year ->", current.year)
print("Month ->", current.month)
print("Day ->", current.day)
print("Hour ->", current.hour)


# difference between two dates
date1 = datetime.date(2026, 5, 6)
date2 = datetime.date(2026, 1, 1)

difference = date1 - date2
print("Difference between dates ->", difference)

