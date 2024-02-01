"""Ejercicio 11 (recursivo o iterativo)
Hacer un damero de n x m cuadrados, cada uno de ellos de lado x.
Tenga en mente modularizar y utilizar las mejores técnicas vistas
hasta ahora.
¿Puede dibujarlos en color rojo? ¿Puede solicitar al usuario de qué
color dibujar, dentro de un subconjunto seleccionado de colores?"""

import turtle
import random
def inicializar():
    t.speed(10)
    t.penup()
    t.hideturtle()
    t.setx(-int(550 / 2))
    t.sety(int(450/2))
    t.pendown()
    t.showturtle()
    t.pensize(1)

def bajar_uno(cantidad_cuadrados_x):  #funcion que baja una clumna para poder dibujar la siguente fila de cuadrados
    t.hideturtle()
    t.penup()
    t.left(180)
    t.forward(50 * cantidad_cuadrados_x)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.pendown()
    t.showturtle()


def cuadrado(lado):
    if lado == 0:
        t.forward(50)
    else:
        t.forward(50)           #dibuja el cuadrado
        t.left(90)
        cuadrado(lado-1)


def dibujar(cantidad,nivel,color):   #dibuja y pinta
    if cantidad == 0:
        return 0
    else:
        if cantidad%2 == 0 and nivel%2 == 0:   #
            if color == 'RANDOM':
                rgb = []
                rgb.append(int(random.randrange(0, 255)))
                rgb.append(int(random.randrange(0, 255)))
                rgb.append(int(random.randrange(0, 255)))    #asigna un color rgb random
                print(color)
                print(rgb)
                turtle.colormode(255)
                t.fillcolor(rgb)
                t.begin_fill()
                cuadrado(4)      #hace el cuadrado
                t.end_fill()     #cuando termina de dibujar el cuadrado lo rellena
            else:
                t.fillcolor(color)
                t.begin_fill()
                cuadrado(4)
                t.end_fill()
        elif cantidad%2 == 1 and nivel%2 == 1:  #pinta segun el nivel en el que este\
            if color == 'RANDOM':
                rgb = []
                rgb.append(int(random.randrange(0, 255)))
                rgb.append(int(random.randrange(0, 255)))
                rgb.append(int(random.randrange(0, 255)))
                print(color)
                print(rgb)
                turtle.colormode(255)
                t.fillcolor(rgb)
                t.begin_fill()
                cuadrado(4)
                t.end_fill()
            else:
                t.fillcolor(color)
                t.begin_fill()
                cuadrado(4)
                t.end_fill()
        else:
            cuadrado(4)
        dibujar(cantidad-1,nivel,color)


def dibujar_en_y(nivel,cantidad_cuadrados_x,color):
    if nivel==0:
        return 1
    else:
        dibujar(cantidad_cuadrados_x,nivel,color)
        bajar_uno(cantidad_cuadrados_x)
        dibujar_en_y(nivel-1,cantidad_cuadrados_x,color)



t = turtle.Pen()
colores = ['red','blue','cyan','yellow','black','pink','purple','green','RANDOM']
rgb = []
print("dibuja un tablero de m*n y pinta las casillas de forma alternada")
fila = int(input("cantidad de filas:"))
columnas = int(input("cantidad de columnas:"))
num = 1
for i in colores:
    print("{}-{}".format(num,i))
    num+=1
color_select = int(input("elija un color segun su numero:"))
color_select = colores[color_select-1]
print(color_select)
inicializar()
dibujar_en_y(fila,columnas,color_select)
turtle.done()
