
from Recepcion import *

re = Recepcion()
re.Lista_Veterinario_cola()
re.nuevo_paciente('Richard Assmann','mascota','duenio')
re.nuevo_paciente('Erich Hintzsche','mascota','duenio')
re.nuevo_paciente('Carl Sachs','mascota','duenio')
re.nuevo_paciente('Erich Hintzsche','mascota','duenio')
re.nuevo_paciente('Richard Assmann','mascota','duenio')
print(re.cantidad('Richard Assmann'))
veteri =3
re.Lista_Veterinario_cola()
print(re.devolvernombrevet(veteri))

"""try:
    veteri = int(input("seleccione a un veterinario:"))
except ValueError:
    print("seleccione usando los numeros, intente nuevamente")
else:
    Nom_duenio = input("Inrgese su Nombre:")
    Nom_Mascota = input("Ingrese el Nombre de su mascota:")
    Nom_Veteri = re.devolvernombrevet(veteri)
    re.nuevo_paciente(Nom_Veteri, Nom_Mascota, Nom_duenio)"""


"""
recepcion = ColaDeBichitos()
recepcion.listadoctores()"""

"""print("poner mascota y duenia al doc1")
Doctores.get('doctor1').nuevo_paciente({'Aaron':'Mara'})
print("poner mascota y duenia al doc1")
Doctores.get('doctor3').nuevo_paciente({'Aaron':'Neko'})
print("poner mascota y duenia al doc1")
Doctores.get('doctor2').nuevo_paciente({'Aaron':'Piolin'})
print("poner mascota y duenia al doc1")
Doctores.get('doctor1').nuevo_paciente({'Aaron':'Nekop'})"""



"""print(Doctores.get('doctor1').nuevo_paciente({'Aaron':'asdd'}))
"""
