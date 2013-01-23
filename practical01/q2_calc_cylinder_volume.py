#Filename:q2_calc_cylinder_volume.py
#Author:PS
#Created:20130122
#Description:Calc vol of cylinder

rad=float(input("Please enter the radius of the cylinder: "))
ht=float(input("Please enter the height of the cylinder: "))
pi=3.1415926535897932384626
vol=rad*rad*pi*ht
print("The volume is {0:.2f}".format(vol))
