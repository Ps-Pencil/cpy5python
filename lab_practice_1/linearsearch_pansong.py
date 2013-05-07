def linear_search(elements,target):
	for i in range(0,len(elements)):
		if elements[i]==target:
			return i
	return -1