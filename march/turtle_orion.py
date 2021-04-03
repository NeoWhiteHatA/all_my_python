#эта прога выводит звезды созвездия Ориона и дает им имена
import turtle

#задаем развем окна
turtle.setup(400, 600)
#скрываем черепаху
turtle.penup()
turtle.hideturtle()

turtle.speed(1)

#астраиваем цвета
turtle.bgcolor('black')
turtle.pencolor('white')
#создаем константы для звезд
LEFT_SHOULDER_X = - 70
LEFT_SHOULDER_Y = 200
RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180
LEFT_BELSTAR_X = -40
LEFT_BELSTAR_Y = -20
MIDDLE_BELSTAR_X = 0
MIDDLE_BELSTAR_Y = 0
RIGHT_BELSTAR_X = 40
RIGHT_BELSTAR_Y = 20
LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180
RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

#наносим звезды на холст
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)#Левое плечо
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y) #
turtle.dot()
turtle.goto(LEFT_BELSTAR_X, LEFT_BELSTAR_Y)#ЛЕВАЯ ЗВЕЗДА В ПОЯСЕ
turtle.dot()
turtle.goto(MIDDLE_BELSTAR_X, MIDDLE_BELSTAR_Y)#средняя зывезда
turtle.dot()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)#правая звезда
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)#левое колено
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)#правое колено
turtle.dot()
#вывод названий звезд

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)#левое плечо
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)#правое плечо
turtle.write('Хатиса')
turtle.goto(LEFT_BELSTAR_X, LEFT_BELSTAR_Y)#левая звезда в поясе
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELSTAR_X, MIDDLE_BELSTAR_Y)#Средняя звезда
turtle.write('Альнилам')
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)#Правая звезда
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)#левое колено
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)#Правое колено
turtle.write('Ригель')

#нанести линию из левого плеча в левую звезду пояса
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELSTAR_X, LEFT_BELSTAR_Y)
turtle.penup()

#нанести линию из правого плеча в правую звезду пояса
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.penup()

#нанести линию из левой звезды пояса в средню звезду пояса
turtle.goto(LEFT_BELSTAR_X, LEFT_BELSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELSTAR_X, MIDDLE_BELSTAR_Y)
turtle.penup()

#Нанести линию из средней звезды пояса в правую звезду пояса
turtle.goto(MIDDLE_BELSTAR_X, MIDDLE_BELSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.penup()

#Нанести линию из левой звезды пояса в левое колено
turtle.goto(LEFT_BELSTAR_X, LEFT_BELSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

#нанести линию из правой звезды пояса в правое колено
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

#оставить окно открытым
turtle.done()
