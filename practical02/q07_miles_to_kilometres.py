#Filename:q07_miles_to_kilometres.py
#Author:PS
#Created:201302901
#Description:To convert from miles to km

print("{0:<6s}{1:<11s}{2:<11s}{3:<6s}".format("Miles","Kilometers","Kilometers","Miles"))
for i in range(1,11):
	print("{0:<6d}{1:<11.3f}{2:<11d}{3:<6.3f}".format(i,float(i)*1.609,15+i*5,(15+i*5)/1.609))