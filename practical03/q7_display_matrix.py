#Filename:q7_display_matrix.py
#Author:PS
#Created:20130221
#Description:generate random matrix
import random

def print_matrix(n):
	for i in range (0,n):
		for j in range(0,n):
			print(random.randint(0,1)," ",end="")
		print("\n",end="")
	return 0
