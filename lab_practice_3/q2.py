outfile=open("BOWLERS.DAT",'a')

def checkdigit(ID):
	return "%s%s"%(ID,(int(ID[0])*1+int(ID[1])*3+int(ID[2])*6+int(ID[3])*7)%10)

ids=['1234','1233','1231','9583','9194','1948','1842','4294','4857','6458']

for ID in ids:
	outfile.write(checkdigit(ID))
	outfile.write('\n')
outfile.close()