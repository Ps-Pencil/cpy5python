# c
import random
class Player:
	def __init__(self,username,score):
		self.username = username
		self.score = score

player_list = []
for i in range(5000):
	score = random.randint(0,99999)
	username = ''
	length = random.randint(4,10)
	number_length = random.randint(0,length-1)
	for j in range(length - number_length):
		alpha = chr(ord('a') + random.randint(0,25))
		if random.randint(0,1) == 0:
			alpha = alpha.upper()
		username += alpha
	for j in range(number_length):
		digit = random.randint(0,9)
		username += str(digit)
	player_object = Player(username,score)
	player_list.append(player_object)

def quicksort(L):
	if len(L) == 0:
		return []
	else:
		before = []
		after = []
		for i in L[1:]:
			if i.score > L[0].score:
				before.append(i)
			elif i.score < L[0].score:
				after.append(i)
			else:
				if i.username < L[0].username:
					before.append(i)
				else:
					after.append(i)
		return quicksort(before) + [L[0]] + quicksort(after)

sorted_list = quicksort(player_list)

# d
def cmp(a,b):
	if a.score == b.score:
		return a.username < b.username
	else:
		return a.score > b.score

def isPosForInsert(pos,player):
	if cmp(sorted_list[pos - 1],player) and cmp(player,sorted_list[pos]):
		return True
	else:
		return False

def insert(username,score):
	player = Player(username,score)
	left = 0
	right = len(sorted_list)-1
	while(left < right):
		mid = (left + right) // 2
		if isPosForInsert(mid,player):
			sorted_list.insert(mid,player)
			break
		if isPosForInsert(mid + 1, player):
			sorted_list.insert(mid + 1, player)
			break
		if cmp(player,sorted_list[mid]):
			right = mid
		else:
			left = mid


for i in sorted_list[:50]:
	print(i.username, i.score)

insert("abc",99900)
print()
for i in sorted_list[:50]:
	print(i.username, i.score)

# f
score = -1
for i in range(len(sorted_list)):
	if (i != 0 and sorted_list[i].score == sorted_list[i-1].score) or (i != len(sorted_list) -1 and sorted_list[i].score == sorted_list[i+1].score):
		if sorted_list[i].score != score:
			print()
			score = sorted_list[i].score
			print(score, ": ",end = '')

		print(sorted_list[i].username,end = " ")
print()

# g
random_score = sorted_list[random.randint(0,len(sorted_list)-1)].score
pos = 0
left = 0
right = len(sorted_list) - 1
while left < right:
	mid = (left + right) // 2
	if(sorted_list[mid].score == random_score):
		pos = mid
		break
	elif(sorted_list[mid].score > random_score):
		left = mid
	else:
		right = mid
while sorted_list[pos].score - random_score <= 5:
	pos -= 1
pos += 1
while random_score - sorted_list[pos].score <= 5:
	print(sorted_list[pos].username,sorted_list[pos].score)
	pos += 1

# h
random_player = random.randint(0,len(sorted_list)-1)
random_score = sorted_list[random_player].score
random_username = sorted_list[random_player].username
pos = 0
left = 0
right = len(sorted_list) - 1
while left < right:
	mid = (left + right) // 2
	if(sorted_list[mid].score == random_score):
		pos = mid
		break
	elif(sorted_list[mid].score > random_score):
		left = mid
	else:
		right = mid
for i in range(1000):
	if sorted_list[max(pos - i, 0)].username == random_username:
		pos = pos - i
		break
	if sorted_list[min(pos + i, len(sorted_list) -1)] == random_username:
		pos = pos + i
		break
low = max(0,pos - 5)
high = min(pos + 5, len(sorted_list) - 1)
for i in range(low,high+1):
	print(sorted_list[i].username,sorted_list[i].score)

