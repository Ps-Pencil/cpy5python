import random
class Player:
	def __init__(self,username,score):
		self.username = username
		self.score = score
		self.next = None

player_list = dict()
last_username = ''
last_score = ''
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
	try:
		b = player_list[username]
		while(b.next != None):
			b = b.next
		b.next = player_object
	except KeyError:
		player_list[username] = player_object
	last_username = username
	last_score = last_score

def lookup(username):
	try:
		b = player_list[username]
		print(username + "'s score: ")
		while(b.next != None):
			print(b.score,end='\t')
			b = b.next
		print(b.score)
		print()
	except:
		print(username,"Not Found")
lookup("abc123")
lookup(last_username)
