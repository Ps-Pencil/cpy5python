#Filename:q4_print_reverse.py
#Author:Pan Song
#Created:20130225
#Description:print reverse int with recursive 

def reverse_int(num):
	if(num//10==0):
		return num
	return int(str(reverse_int(int(str(num)[1:])))+str(num)[0])


 