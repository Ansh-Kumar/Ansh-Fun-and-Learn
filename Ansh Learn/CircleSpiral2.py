#CircleSpiral1.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]


#Ask the User for their name using a text pop up.
your_name = turtle.textinput("Enter you name", "What is your Name")

for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x + 4) /4), "bold") )
    t.left(92)
  
