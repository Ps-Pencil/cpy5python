#Filename:q5_upper_to_lower.py
#Author:PS
#Created:20130122
#Description:convert an uppercase letter to lower case

a=input("Please enter a letter in uppercase: ")
while(len(a)!=1):
    print("Error!You entered more than 1 character!")
    a=input("Please enter a letter in uppercase: ")
a=chr(ord(a)-ord('A')+ord('a'))
print("The lowercase is ",a)

