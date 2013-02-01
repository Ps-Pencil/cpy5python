#Filename:q11_find_gcd.py
#Author:PS
#Created:201302901
#Description:To find the greatest common divisor

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
min=a
if(min>b):
	min=b
while(min!=1):
	if(a%min==0 and b%min==0 ):
		break
	min-=1
print("The greatest common divisor of {0} and {1} is {2}".format(a,b,min))

