"""copo"""

import turtle

def inicializar(long):
    t.pencolor('black')
    t.speed(10)
    t.penup()
    t.hideturtle()
    t.setx(-int(long/2))
    t.sety(int(long/2))
    t.pendown()
    t.showturtle()
    t.pensize(1)


def limpiar(long):
    t.pensize(2)
    t.pencolor('white')
    t.hideturtle()
    t.forward(long)
    t.backward(long)
    t.showturtle()
    t.pencolor('black')
    t.pensize(1)

def koch(long,nivel):
    if nivel == 0 :
        t.forward(long)
    else:
        koch(long/3, nivel-1)
        limpiar(long/3)
        t.left(60)
        koch(long/3,nivel-1)
        t.right(120)
        koch(long/3,nivel-1)
        t.left(60)
        koch(long/3, nivel-1)


def copokoch(long,nivel):
    for i in range(3):
        koch(long,nivel)
        t.right(120)

t = turtle.Pen()
longitud = 300  #modificar
inicializar(longitud)
for i in range(5):
    copokoch(longitud,i)
turtle.done()
