#print calender of specific month and year
import calendar
year = int(input("Enter the year : "))
month = int(input("Enter thr month : "))
cal = calendar.calendar(year, month)
print(cal)