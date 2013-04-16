#program to validate car plate number
import re
infile = open("INVALID.DAT" , "r")
outfile = open("INVALID.DAT" , "a")

invalid_nums=infile.readlines()

c='.'
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
	pattern=re.compile("[A-Za-z]{2}[A-Za-z]?[0-9]?[0-9]{3}[A-Za-z]")
	if not pattern.match(s):
		print("INVALID!")
		if not s+'\n' in invalid_nums:
			outfile.write(s+'\n')
		return False
	elif not s[-1]==checksum(s):
		c=checksum(s)
		print("INVALID! The last alphabet should be ",c)
		if not s+'\n' in invalid_nums:
			outfile.write(s+'\n')
		return False
	else:
		c=checksum(s)
		print("VALID! The last alphabet is ",c)
		return True


car_plate=input("Enter your car plate number: ")
validate(car_plate.upper())
infile.close()
outfile.close()