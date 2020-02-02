from datetime import datetime
#
# x = datetime.datetime.now()
# print(x)
# s=[1,2,3,4]
# date=datetime.strptime(s,'%m/%d/%y')
# print(date)
# import datetime
#
# x = datetime.datetime(2018, 8, 1)
#
# print(x.strftime("%A"))
# import calendar
# print(calendar.calendar(2032))
# Python program to demonstrate working of formatyear() method

# importing calendar module
import calendar

text_cal = calendar.HTMLCalendar(firstweekday = 0)

year = 2018
# Default value of width is 3

# printing formatyear
p=text_cal.formatyear(year)
file=open('outputhtmlformat.html', 'w')
file.write(p)
file.close()
print("successfully uploaded")