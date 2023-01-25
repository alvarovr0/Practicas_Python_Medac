print("Escriba varios números por teclado y termine con un 0")

totalpar=0
totalimpar=0
num=input("Introduzca un numero ")

if not num.isnumeric():
    print("No es un numero")
    num1=0
else:
    num1=int(num)
    while num1!=0:
        if num1%2==0:
            totalpar=totalpar+1
        else:
            totalimpar=totalimpar+1
        num1=int(input("Introduzca otro número: "))


    print("Hay ", totalpar, " números pares y", totalimpar, " números impares")
