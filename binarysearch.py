# 이진 검색 함수, alist에서 값이 item인 것을 찾음. (korean)
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    steps = 0
  
    while first<=last and not found:
        mid = (first + last)//2
        print "new middle index = ", mid
        steps = steps + 1
        if alist[mid] == item:
            found = True
            print "# of steps = ", steps
            return mid
        else:
            if item < alist[mid]:
                last = mid-1
            else:
                first = mid+1
    return -1

#테스팅에 사용될 리스트 vlist  
vlist=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print vlist

# 값 (2, 13, 31, 89)에 대한 검색 
pos0 = binarySearch(vlist, 2)
pos1 = binarySearch(vlist, 13)
pos2 = binarySearch(vlist, 31)
pos3 = binarySearch(vlist, 89)
