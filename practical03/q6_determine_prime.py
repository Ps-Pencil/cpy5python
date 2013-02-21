#Filename:q6_determine_prime.py
#Author:PS
#Created:20130221
#Description:determine whether a num is prime 
import math

def is_prime(n):
	if(n==1):
		return True
	for i in range(2,int(math.sqrt(n))+1):
		if(n%i==0):
			return False
	return True

c=0
i=2
while c<=1000:
	if(is_prime(i)):
		print(i," ",end="")
		i+=1
		c+=1
		if(c%10==0):
			print("\n",end="")
	else:
		i+=1
	
