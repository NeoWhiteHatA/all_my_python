#игра "Порази меня"
import turtle
from typing import TYPE_CHECKING
#constants
SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600
TARGET_LEFT_X = 100
TARGET_LEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUSH = 270
EAST = 0
WEST = 180

#SETTING WINDOW
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGTH)

#draw forpost
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
turtle.pendown()
turtle.pencolor('green')
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.setheading(SOUSH)
turtle.forward(TARGET_WIDTH)
turtle.penup()


#center turtle
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)


#get angle and force
angle = float(input('Введите угол снаряда: '))
force = float(input('Введите пусковую силу снаряда(1-10): '))

#расчет дистанции
distance = force * FORCE_FACTOR

#задание направления
turtle.setheading(angle)


#запуск снаряда
turtle.pendown()
turtle.pencolor('red')
turtle.forward(distance)

#поразил ли снаряд цель
if (turtle.xcor() >= TARGET_LEFT_X and
    turtle.xcor() <= (TARGET_LEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LEFT_Y and 
    turtle.ycor() <= (TARGET_LEFT_Y + TARGET_WIDTH)):
        print('Цель поражена!')
else:
        print('Вы промазали')

#
