"""Ejercicio 3
Realizar un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes
de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.
Siempre se debe dar el menor número de billetes posibles (para 100€ entregaría un único billete, no diez de 10€)"""

def desglose (monto):

    entrega = [0,0,0,0,0,0,0,0,0]  # cada posición representa a la cantidad de billetes que se va a devolver
    while monto != 0:
        if monto >= 500:
            entrega[0] +=1  #le sumo uno a la cantidad de billetes que hay que devolver, segun su posicion y denominacion
            monto = monto - 500

        elif monto >= 200 and monto < 500:
            entrega[1] +=1
            monto = monto - 200

        elif monto >= 100 and monto < 200:
            entrega[2] +=1
            monto = monto - 100

        elif monto >= 50 and monto < 100:
            entrega[3] +=1
            monto = monto - 50

        elif monto >= 20 and monto < 50:
            entrega[4] +=1
            monto = monto - 20

        elif monto >= 10 and monto < 20:
            entrega[5] +=1
            monto = monto - 10

        elif monto >= 5 and monto < 10:
            entrega[6] +=1
            monto = monto - 5

        elif monto >= 2 and monto < 5:
            entrega[7] +=1
            monto = monto - 2

        elif monto == 1:
            entrega[8] +=1
            monto = monto - 1

    return entrega


billete = [500,200,100,50,20,10,5,2,1]
print ("que cantidad de dinero va a pedir")
monto = 1
while monto != 0:
    print("ingrese un monto de 0 para terminar")
    try:
        monto = int(input("€:"))
        if monto < 0:
            print("ingrese una cantidad positiva de dinero")
        elif monto == 0:
            print("saliendo...")
        else:
            if monto in billete:
                if monto <= 2:
                    print("1na moneda de {}".format(monto))
                else:
                    print("1 billete de {}".format(monto))
            else:
                entrega = desglose(monto)
                """print(billete) #control
                print(entrega)"""

                for i in range(0, 9):
                    if entrega[i] > 0:  # no muestra si la cantidad de billetes a devolver es = 0
                        if entrega[i] == 1:
                            if i == 7 or i == 8:
                                print("{}  moneda de €{}".format(entrega[i], billete[i]))
                            else:
                                print("{}  billete de €{}".format(entrega[i], billete[i]))
                        else:
                            if i == 7 or i == 8:  # para distinguir entre monedas y billetes
                                print("{}  monedas de €{}".format(entrega[i], billete[i]))
                            else:
                                print("{}  billetes de €{}".format(entrega[i], billete[i]))

            op = input("Desea hacer otra extracion de dinero?(s/n) :")
            op = op.lower()
            if op == 'n':
                monto = 0
                print("Saliendo")
    except ValueError:
        print("--Error: intente nuevamente\n")

