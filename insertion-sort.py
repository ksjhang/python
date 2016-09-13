def insert(x): 
	for i in range(1, len(x)): 
		j=i-1
		key = x[i]
		while((x[j] > key) and (j >=0)): 
			x[j+1] = x[j] 
			j = j-1
		x[j+1] = key
	return x

vlist = [1, 6, 2, 8, 10, 9, 12, 1, 16, 22, 11, 4,5,3, 6, 0, 3, 99, 21, 0, 6]
print(vlist)
vlist = insert(vlist)
print(vlist)
