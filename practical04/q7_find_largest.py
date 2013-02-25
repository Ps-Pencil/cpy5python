#Filename:q7_find_largest.py
#Author:Pan Song
#Created:20130225
#Description:find largest number in an array

def find_largest(alist):
	if(len(alist)==1):
		return alist[0]
	Max=find_largest(alist[1:])
	if(alist[0]>Max):
		return alist[0]
	else:
		return Max

alist=[5,1,8,7,2]
print(find_largest(alist))