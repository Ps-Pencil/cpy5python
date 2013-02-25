#Filename:q5_count_letter.py
#Author:Pan Song
#Created:20130225
#Description:find number of a letter in a word

def count_letter(String,Letter):
	num=0
	if(String[0]==Letter):
		num=1
	if(len(String)==1):
		return num
	return num+count_letter(String[1:],Letter)

print count_letter("Welcome",'e')