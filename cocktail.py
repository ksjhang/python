def exchange(list, i, j):  
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
def selection(list, l, r):
    while(l < r):
        min = l
        max = l
        for j in range(l+1, r):  
            if list[j] < list[min]:
                min = j
        exchange(list, l, min) 
 for j in range(l+1, r):    
            if list[j] > list[max] :
                max = j
  exchange(list, r-1, max)
  l = l + 1
  r = r - 1
        
vlist = [1, 6, 2, 8, 10, 9, 12, 1, 16, 22, 11, 4,5,3, 6, 0, 3, 99, 21, 0, 6];
print(vlist)
selection(vlist, 0, len(vlist))
print(vlist)

