from turtle import*
from random import*
from math import*
from sys import*

canvas=Screen()
t=Turtle()
t1=Turtle()
t2=Turtle()
t3=Turtle()
t4=Turtle()
t4.ht()



canvas.addshape("rocketship.gif")
t.shape("rocketship.gif")
t.st()
t1.ht()
t2.ht()
t3.ht()

t.pu()
t.lt(90)
t.goto(0, -150)
t1.lt(90)

def right():
  t.rt(90)
  t.fd(10)
  t.lt(90)

def left():
  t.lt(90)
  t.fd(10)
  t.rt(90)

def blast():
  t1.goto(t.xcor(),t.ycor())
  for i in range(400):
    canvas.tracer(0,20)
    t1.pu()
    t1.fd(2)
    t1.pd()
    t1.dot(10,'red')
    canvas.update()
    t1.clear()
    if abs(t2.xcor()-t1.xcor())<5 and abs(t2.ycor()-t1.ycor())<5:
      t2.write('You killed me',font=('Arial',30))
      
      

canvas.onkey(blast, 'space') 
canvas.onkey(left,  'left')
canvas.onkey(right, 'right')
canvas.listen()


def ball1():
  t2.lt(90)
  t2.goto(0, 200)
  for bobby in range(375):
    t2.pu()
    t2.pd()
    canvas.tracer(0)
    t2.pu()
    t2.bk(1)
    t2.pd()
    t2.dot(25,'blue')
    canvas.update()
    t2.clear()


def ball2():
  t3.lt(90)
  t3.goto(100, 200)
  for bobby in range(100):
    t3.pu()
    t3.pd()
    canvas.tracer(0)
    t3.pu()
    t3.bk(3)
    t3.pd()
    t3.dot(15,'blue')
    canvas.update()
    t3.clear()
    if abs(t3.xcor()-t.xcor())<5 or abs(t2.xcor()-t.xcor())<5 and abs(t3.ycor()-t.ycor()) or abs(t2.ycor()-t.ycor()):
      t,ht()
      t4.st()
      t4.write("DESTROYED! GAME OVER!", align='center', font = ("Arial", 12))
      exit()


for blank in range(10):
  ball1()
  ball2()


