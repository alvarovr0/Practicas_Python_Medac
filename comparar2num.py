print("Introduce 2 numeros por teclado")
num1=int(input("Escribe el primer numero "))
num2=int(input("Escribe el segundo numero "))
if num2==num1:
    print("Los numeros son iguales")
else:
    if num2>num1:
        print("El mayor es ", num2)
    else:
        print("El mayor es ", num1)
