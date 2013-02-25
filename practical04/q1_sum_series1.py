#Filename:q1_sum_series1.py
#Author:Pan Song
#Created:20130225
#Description:Sum a series

def m(i):
	if(i==1):
		return 1
	else:
		return 1.0/i+m(i-1)

print(m(3))