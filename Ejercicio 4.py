print("Divisores de un número")

numero = int(input("Introduce un número "))
contador = 0

for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("Tiene ",contador," divisores")