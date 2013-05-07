scores=open("SCORES.DAT",'r')



def minimum(a,b):
	return a if a<b else b

top=[]
for k in range(10):
	player=scores.readline()[:-1]
	player=player.split(',')
	player=player[:-1]+[float(player[2])/float(player[1])]

	if len(top)<1:
		top.append(player)
	else:
		for i in range(minimum(len(top),3)):
			if player[2]>top[i][2]:
				top.insert(i,player)
				break

for i in range(minimum(len(top),3)):
	print("The No. ",i+1," is player ",top[i][0]," with average of {0:.2f}".format(top[i][2]))

scores.close()