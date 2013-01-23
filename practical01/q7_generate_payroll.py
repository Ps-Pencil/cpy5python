#Filename:q7_generate_payroll.py
#Author:PS
#Created:20130122
#Description:generate payroll for given info

name=input("Enter name: ")
hrs=int(input("Enter number of hours worked weekly: "))
pr=float(input("Enter hourly pay rate: "))
CPF=float(input("Enter CPF contribution rate(%): "))

print("Payroll statement for ",name)
print("Number of hours worked in week ",hrs)
print ("Hourly pay rate: $",pr)
print("Gross pay = ${0:.2f}".format(hrs*pr))
print("CPF contribution at ",int(CPF),"% = ${0:.2f}".format(hrs*pr*CPF/100))
print("Net pay = ${0:.2f}".format(hrs*pr-hrs*pr*CPF/100))
