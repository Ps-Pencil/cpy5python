filename=input("Enter the name of the file: ")
infile=None
while not infile:
	try:
		infile=open(filename,'r')
	except IOError:
		print("File does not exist")
		filename=input("Enter the name of the file: ")