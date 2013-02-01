#Filename:q05_find_month_days.py 
#Author:PS
#Created:201302901
#Description:To find the days of a month in a year

days=[31,28,31,30,31,30,31,31,30,31,30,31]

year=int(input("Enter a year: "))
month=int(input("Enter a month: "))

leap=0
if (year%4==0 and year%100!=0) or year%400==0:
	leap=1
if leap==1:
	days[1]=29
print(days[month-1])

