import turtle
t = turtle.Turtle()
win = turtle.Screen()
t.pensize(5)
t.pencolor("blue")
t.fillcolor("red")
t.penup()
t.setpos(-200,-100)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()
t.penup()
t.setpos(0,0)
t.pendown()
t.pensize(1)
t.fillcolor("white")
t.pencolor("white")
t.begin_fill()
t.forward(30)
t.left(60)
t.forward(30)
for i in range(6):
    t.left(120)
    t.forward(30)
    t.right(60)
    t.forward(30)
t.end_fill()
t.hideturtle()
win.exitonclick()