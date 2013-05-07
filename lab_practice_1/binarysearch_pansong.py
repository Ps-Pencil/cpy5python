def binary_search(A,target,low,high):
	mid=(low+high)/2
	if low>high:
		return -1
	if A[mid]==target:
		return mid
	elif A[mid]<target:
		return binary_search(A,target,mid+1,high)
	else:
		return binary_search(A,target,low,mid-1)

