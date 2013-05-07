import re


bowlers=[]
highest=0
wrong=False
i=0
while(i<10):
	if not wrong:
		bowler=input("Please enter the ID and score (separated by space) for bowler no. %s. Do not enter anything to end input: "%(i+1))
	wrong=False
	ID=re.compile("[0-9]{4}")
	error=""
	if bowler=="" and i==0:
		error="You need at lease 1 input"
	elif bowler=="":
		break
	bowler=bowler.split(' ')
	#comment out the following 3 lines if allow entering players with same id
	for bowl in bowlers:
		if bowl[0]==bowler[0]:
			error="Player with the same ID already exists"
	if not error:
		if (len(bowler)!=2):
			error="Please enter two numbers"
		elif not(bowler[0].isdigit() and bowler[1].isdigit()):
			error="Please enter two numbers"
		elif not ( ID.match(bowler[0]) and int(bowler[1])>=0 and int(bowler[1])<=300):
			error="Please enter the info in correct format. ID must be four digits. score must be 0-300 inclusive"
	if error:
		#print (i)
		print(error)
		bowler=input("Please enter the ID and score (separated by space) for bowler no. %s again: "%(i+1))
		#print (i)
		wrong = True
		continue

	bowlers.append(bowler)
	if int(bowler[1])>int(bowlers[highest][1]):
		#print (i,highest)
		highest=i
	i+=1

print("Player %s has a highest score of %s"%(bowlers[highest][0],bowlers[highest][1]))

