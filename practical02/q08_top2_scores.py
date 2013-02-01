#Filename:q08_top2_scores.py
#Author:PS
#Created:201302901
#Description:To find the student with the highest and second highest score

num=int(input("Enter the No. of students: "))
topname=""
topscore=0
top2name=""
top2score=0
for i in range (1,num+1):
	name=input("Please Enter the name of student {}: ".format(i))
	score=float(input("Please Enter the score of student {}: ".format(i)))
	if(score>topscore):
		topscore=score
		topname=name
	elif(score>top2score):
		top2score=score
		top2name=name
print("{0} has the highest score: {1}".format(topname,topscore))
print("{0} has the second highest score: {1}".format(top2name,top2score))

