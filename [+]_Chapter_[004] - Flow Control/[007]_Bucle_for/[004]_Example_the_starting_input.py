# Crear un código que permite iniciar
# en número y luego indicar hasta que
# número debemos de llegar, indicados
# por teclado. input().

inicio  =   int(input("Ingresar Nº inicial  : "))
final   =   int(input("Ingresar Nº Final    : "))

for i in range(inicio,final):
    print(i)

