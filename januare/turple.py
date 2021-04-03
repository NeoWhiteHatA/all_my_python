import turtle
colors = [ 'red', 'blue', 'purple', 'orange', 'yellow', 'green',]
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(720):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(90)