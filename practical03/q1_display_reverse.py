#Filename:q1_display_reverse.py
#Author:PS
#Created:20130218
#Description:display reverse of a number

def reverse_int(n):
	n=int(str(n)[::-1])
	return n

print(reverse_int(980))