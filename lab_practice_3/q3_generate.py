bowlers_info=open("BOWLERS.DAT",'r')
scores_info=open("SCORES.DAT",'a')

import random

def Generate_scores():
	for i in range(10):
		ID=bowlers_info.readline()
		no_game=random.randint(5,16)
		total_score=0
		for i in range(no_game):
			total_score+=random.randint(0,300)
		scores_info.write("%s,%s,%s\n"%(ID[:-1],no_game,total_score))

Generate_scores()
bowlers_info.close()
scores_info.close()