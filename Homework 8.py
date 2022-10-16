# 060 Нарисуйте квадрат
import turtle

for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()

# 061 Нарисуйте треугольник
import turtle

for i in range(0, 3):
    turtle.forward(50)
    turtle.right(120)

turtle.exitonclick()

# 061 второй способ
import turtle

for i in range(0, 3):
    turtle.forward(50)
    turtle.left(120)

turtle.exitonclick()

# 062 Нарисуйте круг
import turtle

turtle.circle(100)

turtle.exitonclick()


#063 Нарисуйте в один ряд три квадрата, разбелённых промежутками.Заполните их тремя разными цветами
import turtle

turtle.setup(1800,500)   #устанавливаю размер окна для рисования
turtle.color("black", "red")   #устанавливаю цвет контура чёрный, цвет заливки будущей фигуры - красный
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

for i in range(0,1):  #ставлю цикл для промежутка между квадратами
    turtle.forward(100)
    turtle.right(90)
turtle.penup()   #делаю перо невидемым
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.pendown()  #делаю перо видимым
turtle.begin_fill()
turtle.color("black", "yellow")  #устанавливаю цвет контура чёрный, цвет заливки второй фигуры - жёлтый
for i in range(0, 4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.forward(100)
turtle.penup()         #делаю перо невидимым
turtle.forward(100)
turtle.left(90)

turtle.pendown()     #делаю перо видимым
turtle.begin_fill()
turtle.color("black", "green")  #устанавливаю цвет контура чёрный, цвет заливки третьего квадрата - зелёный
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()


#064 Нарисуйте пятиконечную звезду
import turtle

for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()


#065 Нарисуйте цифры, изображённые ниже, начиная от нижней точки цифры 1
import turtle

turtle.setup(1800,500)   #устанавливаю размер окна для рисования
turtle.left(90)   #рисуем цифру 1
turtle.forward(100)
turtle.right(90)

turtle.penup() # Делаю перо невидемым
turtle.forward(100) #перевожу перо для рисования цифры 2

turtle.pendown() #делаю перо видимым
turtle.forward(100)
turtle.right(90)
turtle.forward(60)
turtle.left(270)
turtle.forward(100)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(100)


turtle.penup() # Делаю перо невидемым
turtle.forward(100) #перевожу перо для рисования цифры 3

turtle.pendown() #делаю перо видимым
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.right(270)
turtle.forward(50)
turtle.right(180)

turtle.penup()
turtle.forward(50)
turtle.right(270)
turtle.pendown()

turtle.forward(50)
turtle.left(90)
turtle.forward(100)

turtle.exitonclick()

#066 Нарисуйте 8-угольник, все стороны которого окрашены в разные цвета
# (цвета случайно выбираются из списка возможных)
import turtle
import random

color = ["yellow", "blue", "red", "green", "brown", "purple"]

turtle.begin_fill()

for i in range(0, 8):
    number = random.choice(color)
    turtle.color(number, "white")
    turtle.forward(100)
    turtle.right(45)

turtle.end_fill()

turtle.exitonclick()


#067 Нарисуйте следующий узор
import turtle

for i in range(0, 8):
    turtle.forward(50)
    turtle.right(45)

for i in range(0, 8):
    turtle.forward(50)
    turtle.left(45)

turtle.right(90)

for i in range(0, 8):
    turtle.forward(50)
    turtle.right(45)

turtle.right(90)

for i in range(0, 8):
    turtle.forward(50)
    turtle.left(45)

turtle.left(45)

for i in range(0, 8):
    turtle.forward(50)
    turtle.right(45)

turtle.left(45)

for i in range(0, 8):
    turtle.forward(50)
    turtle.left(45)

turtle.right(90)

for i in range(0, 8):
    turtle.forward(50)
    turtle.right(45)

turtle.left(135)

for i in range(0, 8):
    turtle.forward(50)
    turtle.left(45)


turtle.exitonclick()

#068 Нарисуйте узор, который меняется при каждом запуске программы.
#Используйте функцию random для выбора количества линий, длины каждой линии и каждого угла поворота.
import turtle
import random

linii = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
ygol = [30,45,50,90,135,150,180,270,360]
lenlin=[25,50,60,70,80,90,100,120,150,130,110,140,160,170,180,190,200]

linii1 = random.choice(linii)
ygol1 = random.choice(ygol)
lenlin1 = random.choice(lenlin)

for i in range(linii1):
    turtle.forward(lenlin1)
    turtle.right(ygol1)


turtle.exitonclick()