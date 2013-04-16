def insertion_sort(a):
    for j in range(1, len(a)):
        num = a[j]
        i = j - 1
        while (i >= 0 and a[i] > num):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = num
    return a
    
x = insertion_sort([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(x)