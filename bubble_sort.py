def bubble_sort(A):
  swapped = True # assume not sorted
  while swapped:
    swapped = False
    for i in range(1,len(A)):
      if A[i-1] > A[i]:
        A[i-1], A[i] = A[i], A[i-1]
        swapped = True
  return A

# main
A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(bubble_sort(A))