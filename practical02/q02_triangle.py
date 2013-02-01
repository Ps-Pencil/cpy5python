#Filename:q02_triangle.py
#Author:PS
#Created:201302901
#Description:To compute the perimeter of a triangle

a=int(input("Enter side 1: "))
b=int(input("Enter side 2: "))
c=int(input("Enter side 3: "))

if a+b>c and a+c>b and b+c>a:
	print("Perimeter = ",a+b+c)
else:
	print("Invalid Triangle!")
	