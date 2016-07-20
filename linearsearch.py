import turtle

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
    
# 선형 검색 함수, 리스트(llist)와 찾으려는 키값(key)을 인자로 필요로 함
def linear_search(llist, key):
      for k in range(len(llist)):
        if llist[k] == key:
            print "found ", key, " at ", str(k)
            return k  
    
# 리스트(list)의 특정 위치(pos)에서 멈춤을 표시함
def stop_at(t, pos, list):
    ind=0
    for i in list :
      t.goto(i+20,0)
      # 그리기 속도를 느리게 해서 잘 보이게 함
      t.speed(1)
      t.dot(10)
      if ind == pos :
        print "found"
        break 
      ind = ind + 1

# 여기서부터 수행함, 위는 사용될 함수들에 대한 코드임.

# 터틀 그래픽스 초기화
t = turtle.Turtle()

# 정상 그리기 속도
t.speed(110)

# 원소들의 위치, 중앙이 0, 7개 원소를 가정함.
# list = [-150,-100,-50,0,50,100, 150]
list = [-250, -200, -150,-100,-50,0,50,100, 150, 200, 250]

# 예제 리스트 원소들
# mylist = ['A', 'X', 'B', 'Y', 'Z', 'T', 'K']
mylist = ['A', 'X', 'B', 'Y', 'Z', 'T', 'K', 'C', 'E', 'F', 'G']

ind=0
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

# 선형 검색
pos = linear_search(mylist, 'E')
# 선형 검색으로 찾은 위치에서 멈춤 표시
stop_at(t, pos, list)
