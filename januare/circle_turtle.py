import turtle
t = turtle.Pen()
turtle.bgcolor('black')
sides = 12

colors = ['red', 'salmon', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'white', 'gold', 'brown', 'silver']
for x in range(360):
    t.pencolor(colors [x%sides])
    t.forward(x * 2/sides + x)
    t.left(720/sides + 1)
    t.width(x * sides/200)
    t.left(90)