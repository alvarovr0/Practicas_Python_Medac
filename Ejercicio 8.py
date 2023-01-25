print("Piramide de números")

altura = int(input("Introduce un número "))


for i in range(1, altura+1):
    espacios = " " * (altura - i)
    numeros = ""
    for j in range(1, i+1):
      numeros += str(j)
    for j in range(i-1, 0, -1):
      numeros += str(j)
    print(espacios + numeros)