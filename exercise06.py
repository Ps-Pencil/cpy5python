import datetime
import re

today=datetime.date.today()
print today.strftime("%d-%m-%Y")
print today.strftime("%d%m%y")
print today.strftime("%y%m%d")
print today.strftime("%A %d %B %Y")
print today.strftime("%a %d %b %Y")



#exercise 2
while(1):
	nric=input("Please Enter your NRIC:")
	name=input("Please Enter your name: ")
	cls=input("Please Enter your class: ")
	gender=input("Gender?:")
	dob=input("Enter your date of birth in the format DD-MM-YYYY: ")
	weight=input("Enter your weight(kg): ")
	height=input("Enter your height(cm): ")

	have_error=False
	msg="Ok Thank you"

	pattern_nric=re.compile("^[GgSs][0-9]{7}[a-zA-Z]$")
	pattern_class=re.compile("^[1][123][Yy][123456][cC][1234][12345]$")
	if not cls:
		have_error=True
		msg="Class cannot be empty!"
	elif not pattern_class.match("cls"):
		have_error=True
		msg="Class format Incorrect"
	elif not



	if not have_error:
		break
	