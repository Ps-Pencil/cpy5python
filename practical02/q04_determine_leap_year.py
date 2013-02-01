#Filename:q04_determine_leap_year.py
#Author:PS
#Created:201302901
#Description:To determine whether a year is a leap year

year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or year%400==0:
	print("Leap")
else:
	print("Not leap")
