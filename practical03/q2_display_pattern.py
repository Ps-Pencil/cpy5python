#Filename:q2_display_pattern.py
#Author:PS
#Created:20130218
#Description:display certain patterns

def display_pattern(n):
	s=""
	for i in range(1,n+1):
		s=s+" "+str(i)
	length=len(s)
	for i in range(1,n+1):
		s=""
		for j in range (i,0,-1):
			s+=" "+str(j)
		print("{0:>{1}s}".format(s[1:],length-1))
	return 0

display_pattern(15)