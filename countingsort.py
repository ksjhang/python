def countsort(listin):
# calculate the histogram of key frequencies:
	count = [0,0,0,0,0,0,0,0,0,0]
	for x in range(len(listin)):
		count[listin[x]] += 1
	print("counts ", count)
# calculate the starting index for each key:
	total = 0
	for i in range(10):   # i = 0, 1, ... k-1
		counti = count[i]
		count[i] = total
		total += counti
	print("pos = ", count)
# copy to output array, preserving order of inputs with equal keys:
	listout = [ 0 for x in range(len(listin))]
	for x in range(len(listin)):
		listout[count[listin[x]]] = listin[x]
		count[listin[x]] += 1
	return listout

vlist = [1,3,2,4,3,5,4,6,7,8,6,5,4,3,2,1,5,8,9,7,6,5,4,3,4,6,1,8,0,9,8]
print(vlist)
vvlist = countsort(vlist)
print(vvlist)

