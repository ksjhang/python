def quicksort(x):
	if len(x) <= 1:
		return x

	pivot = x[len(x)//2]
	less = []
	more = []
	equal = []
	for a in x:
		if a < pivot:
			less.append(a)
		elif a > pivot:
			more.append(a)
		else:
			equal.append(a)

	return quicksort(less) + equal + quicksort(more)
    
vlist = [1, 6, 2, 8, 10, 9, 12, 1, 16, 22, 11, 4,5,3, 6, 0, 3, 99, 21, 0, 6]
print(vlist)
vlist = quicksort(vlist)
print(vlist)
