import turtle
def binarySearch(alist, item, list):
    first = 0
    last = len(alist)-1
    found = False
    steps = 0
    t.speed(1)
    t.penup()
    
    while first<=last and not found:
        mid = (first + last)//2
        print "new middle index = ", mid
        t.goto(list[mid]+20,0)
        t.dot(10)
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

# 사각형 그리는 함수, 색상(color), 크기(xsize, ysize), 위치(sx,sy) 
def draw_rect(turtle, color, xsize, ysize, sx, sy):
    turtle.penup()
    turtle.pensize(3)
    turtle.pencolor(color)
    turtle.goto(sx,sy)
    turtle.pendown()
    turtle.forward(xsize)
    turtle.left(90)
    turtle.forward(ysize)
    turtle.left(90)
    turtle.forward(xsize)
    turtle.left(90)
    turtle.forward(ysize)
    turtle.left(90)


t = turtle.Turtle()
t.speed(110)
mylist = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'J', 'K', 'Y', 'Z']
ind=0
list = [-250, -200, -150,-100,-50,0,50,100, 150, 200, 250]

# 사각형 그리기와, 사각형 안에 글짜 쓰기
for i in  list :
  draw_rect(t,'blue',30,30,i,0)
  t.penup() 
  t.forward(10) 
  t.left(90) 
  t.forward(10) 
  t.write(mylist[ind])
  t.right(90)
  ind = ind + 1

t.penup() 

pos0 = binarySearch(mylist, 'Z', list)
print "mylist[" , pos0,  "]"


