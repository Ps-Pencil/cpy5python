#Filename:q06_kilograms_to_pounds.py
#Author:PS
#Created:201302901
#Description:To convert from kg to pounds

print("{0:<10s}{1:<10s}".format("Kilograms","Pounds"))
for i in range(1,11):
	print("{0:<10d}{0:<10.1f}".format(i,float(i)*2.2))
