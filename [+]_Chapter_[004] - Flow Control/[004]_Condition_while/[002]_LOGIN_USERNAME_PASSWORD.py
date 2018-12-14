
# CREATED OF LOGIN USERNAME AND PASSWORD

count   =   1

while count <= 3:
    print("INTENTO : ", count)
    username = input("USERNAME: ")
    password = input("PASSWORD: ")

    if username == "admin" and password == "123":
        print("ACCESO PERMITIDO")
        break

    else:
        print("INTENTELO NUEVAMENTE")
        count = count + 1

if count > 3:
    print("ACCESO BLOQUEADO")




