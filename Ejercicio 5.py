print("Pequeño, mediano y grande")

num1=int(input("Introduce el primer número "))
num2=int(input("Introduce el segundo número "))
num3=int(input("Introduce el tercer número "))

if num1==num2 and num2==num3:
    print("Los 3 números son iguales")
if num1==num2 and num2!=num3:
    if num2>num3:
        print("El mayor es: ",num2)
        print("El menor es: ",num3)
        print("No hay termino medio")
    else:
        print("El mayor es: ",num3)
        print("El menor es: ",num2)
        print("No hay termino medio")
if num1!=num2 and num2==num3:
    if num2>num1:
        print("El mayor es: ",num2)
        print("El menor es: ",num1)
        print("No hay termino medio")
    else:
        print("El mayor es: ",num1)
        print("El menor es: ",num2)
        print("No hay termino medio")
if num1!=num2 and num2!=num3:
    if num1<num2 and num1<num3:
        print("El pequeño es: ",num1)
        if num2<num3:
            print("El mediano es: ", num2)
            print("El grande es: ", num3)
        else:
            print("El mediano es: ", num3)
            print("El grande es: ", num2)
            
    if num2<num1 and num2<num3:
        print("El pequeño es: ",num2)
        if num1<num3:
            print("El mediano es: ", num1)
            print("El grande es: ", num3)
        else:
            print("El mediano es: ", num3)
            print("El grande es: ", num1)
            
    if num3<num1 and num3<num2:
        print("El pequeño es: ", num3)
        if num1<num2:
            print("El mediano es: ", num1)
            print("El grande es: ", num2)
        else:
            print("El mediano es: ", num2)
            print("El grande es: ", num1)
