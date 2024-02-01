"""Ejercicio 13
Escribir el código para dibujar una curva de Koch, utilizando recursión

                 adelante    atras      rotar   para dar angulos
mover dibujar  = forard()   backward()      right()   left()             setx()

control del lapiz = penup()    pendown()    pencolor()    pensize()

estado de la tortuga = hideturtle()     showturtle()

"""


import turtle

def inicializar(long):
    turtle.bgcolor('black')
    t.color('white')
    t.speed(10)
    t.penup()
    t.hideturtle()
    t.setx(-int(long/2))
    t.pendown()
    t.showturtle()
    t.pensize(1)

def koch(long,nivel):
    if nivel == 0 :
        t.forward(long)
    else:
        koch(long/3, nivel-1)
        t.left(60)
        koch(long/3,nivel-1)
        t.right(120)
        koch(long/3,nivel-1)
        t.left(60)
        koch(long/3, nivel-1)


t = turtle.Pen()
longitud = 800  #modificar
inicializar(longitud)
koch(longitud,3)
turtle.done()







