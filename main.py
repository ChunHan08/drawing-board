from turtle import *
forward(100)
speed(11)
shape("turtle")
import turtle
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
import turtle
polygon = turtle.Turtle()
num_sides = 6
side_lenght = 70
angle = 360.0 / num_sides
for i in range(num_sides):
  polygon.forward(side_lenght)
  polygon.right(angle)
turtle.done()
pensize(20)
pencolor('red')
forward(50)
pencolor(0, 1.0, 0)
forward(50)
pencolor((0, 0.5, 0.5))
forward(50)
pensize(10)
goto(-400, 50)
for red in range(4):
  for green in range(4):
    for blue in range(4):
      pencolor(red/4.0, green/4.0, blue/4.0)
      forward(10)