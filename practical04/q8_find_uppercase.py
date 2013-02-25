#Filename:q8_find_uppercase.py
#Author:Pan Song
#Created:20130225
#Description:return number of uppercase letters

def find_num_uppercase(String):
	num=0
	if(String[0].isupper()):
		num=1
	if(len(String)==1):
		return num
	return num+find_num_uppercase(String[1:])

print(find_num_uppercase('Good MorninG!'))