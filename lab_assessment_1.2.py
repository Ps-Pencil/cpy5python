#mysterycarplate.py
import re

def checksum(s):
	mapping=['A', 'Y', 'U', 'S', 'P', 'L', 'J', 'G', 'D', 'B', 'Z', 'X', 'T', 'R', 'M', 'K', 'H', 'E', 'C']
	if not s[2].isdigit():
		s=s[1:]
	if len(s)<7:
		s=s[:2]+'0'+s[2:]
	weights=[14, 2, 12, 2, 11, 1]
	sums=0
	for i in range(0,6):
		n=0
		if s[i].isdigit():
			n=int(s[i])
		else:
			n=ord(s[i])-ord('A')+1
		sums+=n*weights[i]
	remainder=sums%19
	return mapping[remainder]

def validate(s):
	#print(s)
	if not s[-1]==checksum(s):
		return False
	return True
s='SBV686aJ'
for i in range(0,10):
	if validate(s[:6]+str(i)+s[7:]):
		print(str(i)+' '+s[:6]+str(i)+s[7:])
s='EW33b3C'
for i in range(0,10):
	if validate(s[:4]+str(i)+s[5:]):
		print(str(i)+' '+s[:4]+str(i)+s[5:])