from quicksort_pansong import *
from binarysearch_pansong import *
input_str=raw_input("Please enter up to 5 numbers: ")
input_list=input_str.split(' ')
num_list=[]
error=False
for i,num in enumerate(input_list):
	if not error and not num.isdigit():
		print "Please do not enter things other than numbers."
		error=True
	else:
		if not error and int(num)<0 or int(num) > 100:
			print "Please do not enter numbers out of the range 0-100"
			error=True
		else:
			num_list.append(int(num))

if not error and len(num_list)>5:
	print "Please do not enter more than 5 numbers. "
	error=True

if not error and num_list:
	num_list=quick_sort(num_list)
	print "The sorted list is " , num_list

	#binary search the item
	target=input("Enter the number you want to search: ")
	while not target:
		target=input("Number is Empty. Please enter again: ")
	
	if binary_search(num_list,int(target),0,len(num_list)-1)==-1:
		print("Not Found")
	else:
		print "Number found at position ", binary_search(num_list,int(target),0,len(num_list)-1)