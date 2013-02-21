#Filename:q3_find_gcd.py
#Author:PS
#Created:20130218
#Description:display the greatest common divisor

def gcd(m,n):
	if m<n:
		m,n=n,m
	if m%n==0:
		return n
	return gcd(n,m%n)