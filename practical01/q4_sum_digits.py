#Filename:q4_sum_digits.py
#Author:PS
#Created:20130122
#Description:Calc the sum of all the digits of an integer

num=int(input("Please enter a number between 1 and 1000: "))
sum=0
while (num!=0):
    sum+=num%10
    num=num//10
print("The sum of all the digits is ",sum)
