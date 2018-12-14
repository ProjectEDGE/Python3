# Crear un programa que solicite los
# siguiente datos: Nombre, apellido y edad.
# Luego debemos de configurar si desea salir.
# y mostrar los datos ingresados.

# Para Salir del programa debemos de utilizar
# el módulo sys.

import sys

while True:

    nombre      =   input("Ingresar su Nombre   : ")
    apellido    =   input("Ingresar su Apellido : ")
    edad        =   int(input("Ingresar su Edad : "))

    salir       =   input("Que desea hacer [S] - Salir / [R] - Registrar: ")

    if salir == "S" or salir == "s":
        print("REGISTROS")
        print("Su Nombre es   : ", nombre)
        print("Su Apellido es : ", apellido)
        print("Su Edad es     : ", edad)
        sys.exit()


