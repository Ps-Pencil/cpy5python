#Filename:CP_BMI.py
#Author:PS
#Created:20130121
#Description:To Calc BMI

#prompt and get weight
mass=int(input("Please enter your weight(kg): "))
#prompt and get height
height=float(input("Please enter your height(m): "))
#calculate bmi
bmi=mass/(height**2)
#display result
print("Your BMI is: {0:.2f}".format(bmi))


