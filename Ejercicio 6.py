print("Piramide de *")

altura = int(input("Introduce un número "))
asteriscos = 1

for espacios in range(altura, 0, -1):

    for e in range(espacios):
        print("  ", end="")

    for a in range(asteriscos):
        print("* ", end="")

    print()
    asteriscos+=2