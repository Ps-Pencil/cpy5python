#Filename:q2_sum_series2.py
#Author:Pan Song
#Created:20130225
#Description:Sum a series

def m2(i):
	if(i==1):
		return 1.0/3
	else:
		return i/(2.0*i+1.0)+m(i-1)

