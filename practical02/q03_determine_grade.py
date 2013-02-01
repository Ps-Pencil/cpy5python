#Filename:q03_determine_grade.py
#Author:PS
#Created:20133001
#Description:To determine the grade of a score

score = int(input("Please enter a score: ))
while score>100 or score < 0 :
	print("Invalid! Score must be within 0 - 100.")
	score = int(input("Please enter a score: ))
if score>=70:
	print("A")
elif score >=60:
	print("B")
elif score >=55:
	print("C")
elif score >=50:
	print("D")
elif score >=45:
	print("E")
elif score >=35:
	print("S")
else :
	print("U")
