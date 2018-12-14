while True:
    print("Quién eres tú: ")    # Imprimir por pantalla
    nombre = input()              # Ingresamos un nombre

    if nombre != "joe":
        continue
        print("Hello, Joe. What us the password? (It is a fish.)")
    password = input()

    if password == "swordfish":
        break

print("Access granted.")