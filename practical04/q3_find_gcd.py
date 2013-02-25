#Filename:q3_find_gcd.py
#Author:Pan Song
#Created:20130225
#Description:find gcd 

def gcd(m,n):
	if m<n:
		m,n=n,m
	if m%n==0:
		return n
	return gcd(n,m%n)

print(gcd(24,16))
print(gcd(255,25))
