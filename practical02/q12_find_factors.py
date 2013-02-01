#Filename:q12_find_factors.py
#Author:PS
#Created:201302901
#Description:To find the smallest factors of a number

factors=[]
n=int(input("Enter a number: "))

while(n!=1):
	i=2
	while(i<=n):
		if(n%i==0):
			factors.append(i)
			n/=i
			break
		i+=1

#print(factors[0],end="")
#for i in factors[1:]:
#	print(",",i,end="")
#print("\n")
print(",".join(str(i) for i in factors))

