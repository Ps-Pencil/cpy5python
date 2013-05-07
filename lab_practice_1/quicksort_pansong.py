def quick_sort(A):
	if len(A)==0:
		return []
	else:
		return quick_sort([i for i in A[1:] if i < A[0]]) + [A[0]] + quick_sort([i for i in A[1:] if i >= A[0]])
