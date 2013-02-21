#Filename:q8_convert_milliseconds.py
#Author:PS
#Created:20130221
#Description:convert ms to hrs min s

def convert_ms(n):
	hrs=n//3600000
	minutes=(n%3600000)//60000
	seconds=(n%60000)//1000
	s=str(hrs)+":"+str(minutes)+":"+str(seconds)
	return s

print(convert_ms(555550000))