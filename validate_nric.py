import re

def generate_check_letter(s):
	tot=0
	weight=[2,7,6,5,4,3,2]
	k=0
	for i in s[1:-1]:
		tot+=int(i)*weight[k]
		k+=1
	if s[0]=='T' or s[0]=='G':
		tot+=4
	tot%=11
	dict_S_T=['J','Z','I','H','G','F', 'E', 'D','C','B','A']
	dict_F_G=['X','W','U', 'T','R','Q', 'P','N','M','L','K']
	if s[0]=='S' or s[0]=='T':
		return dict_S_T[tot]
	else:
		return dict_F_G[tot]

def validate_nric(s):
	print(generate_check_letter(s))
	pattern=re.compile("[GgTtSsFf][0-9]{7}[A-Za-z]")
	if int(s[1:3])>=40 and int(s[1:3])<=67:
		return False
	if not pattern.match(s):
		return False
	if s[-1]!=generate_check_letter(s):
		return False
	return True

while(1):
	nric=input("Enter your NRIC: ")
	if nric=="end":
		break
	if validate_nric(nric.upper()):
		print ("Valid!")
	else:
		print ("Invalid")
	