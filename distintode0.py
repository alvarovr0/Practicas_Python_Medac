print("Escriba varios números por teclado y termine con un 0")

suma=0
contador=0
num=input("Introduzca un numero ")

if not num.isnumeric():
    print("No es un numero")
    num1=0
else:
    num1=int(input("Introduzca el primer número: "))

    while num1!=0:
        suma=suma+num1
        contador=contador+1
        num1=int(input("Introduzca otro número: "))

    media=suma/contador

    print("La media es ", media)
