import random

def Girar_Numero(Respuesta):
    if Respuesta == 1:
        return "Ganador el Nº 1"
    elif Respuesta == 2:
        return "Ganador el Nº 2"
    elif Respuesta == 3:
        return "Ganador el Nº 3"
    elif Respuesta == 4:
        return "Ganador el Nº 4"
    elif Respuesta == 5:
        return "Ganador el Nº 5"
    elif Respuesta == 6:
        return "Ganador el Nº 6"
    elif Respuesta == 7:
        return "Ganador el Nº 7"
    elif Respuesta == 8:
        return "Ganador el Nº 8"
    elif Respuesta == 9:
        return "Ganador el Nº 9"

# Opción 1
print(Girar_Numero(random.randint(1,9)))

# Opción 2
#girar =  random.randint(1,9)
#premiado = Girar_Numero(girar)
#print(premiado)