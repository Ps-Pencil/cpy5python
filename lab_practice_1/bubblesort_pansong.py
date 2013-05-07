def bubble_sort(A):
	for i in range(len(A),1,-1):
		swapped=False
		for j in range(1,i):
			if A[j-1]>A[j]:
				A[j-1],A[j]=A[j],A[j-1]
				swapped = True
		if not swapped:
			break
	return A