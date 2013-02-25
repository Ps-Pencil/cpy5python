#Filename:q6_compute_sum.py
#Author:Pan Song
#Created:20130225
#Description:compute sum of digits of a number


def sum_digits(num):
	if(num//10==0):
		return num
	return num%10+sum_digits(num//10)

print sum_digits(234)