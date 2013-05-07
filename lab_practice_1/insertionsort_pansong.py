def insertion_sort(A):
	for i in range(1,len(A)):
		num=A[i]
		j=i-1
		while j>=0 and A[j]>num:
			A[j+1]=A[j]
			j-=1
		A[j+1]=num
	return A
