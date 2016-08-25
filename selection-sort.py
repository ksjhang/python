def exchange(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
    
def selection(list, l, r):
    for i in range(l,r-1):
        min = i
        for j in range(i+1, r):
            if list[j] < list[min]:
                min = j
        exchange(list, i, min)
        
vlist=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
vlist = vlist[::-1];
print( vlist)

selection(vlist,0,len(vlist))
print(vlist)
