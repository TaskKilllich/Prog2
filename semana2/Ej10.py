"""Ejercicio 10
La función circle(r) del módulo turtle permite dibujar un círculo de radio r.
a. A partir de esta función, implemente el programa
recursivo que permita dibujar la siguiente figura:

b. Escriba el programa que, a partir del módulo
implementado en a., permita dibujar:

"""


import  turtle

def iniciar():
    t.speed(10)
    t.pensize(2)
    turtle.bgcolor('black')
    t.color('cyan')

def drawa(n):
    if n == 0:
        t.hideturtle()
        return 0
    else:
        t.circle(50)
        t.right(36)
        drawa(n-1)

def drawb(n):
    if n == 0:
        t.color('red')
        drawa(10)
    else:
        t.circle(100)
        t.right(36)
        drawb(n-1)

print("a-ejecutar dibujo a\nb-ejecutar dibujo b")
op = input("op:")
t = turtle.Pen()
iniciar()
if op =='a':
    drawa(10)
else:
    drawb(10)
#rotarlo un poco
turtle.done()





