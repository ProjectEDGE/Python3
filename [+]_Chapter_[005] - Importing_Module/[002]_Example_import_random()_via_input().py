# Ejemplo básico de importación de módulo, uso
# del módulo randon(). ingresar por teclado el
# inicio y final de los números a elegir.

import random

inicio  =   int(input("Ingrese Nº Inicio:   "))
final   =   int(input("Ingrese Nº Final :   "))

for i in range(5):
    print(random.randint(inicio,final))

