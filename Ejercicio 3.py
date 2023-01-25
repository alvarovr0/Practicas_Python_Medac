print("Números primos")

x=2
p=0
primo=int(input("Escribe un número "))

while x<primo:
    if primo%x==0:
        p=1
    x=x+1
if p==0:
    print("Es primo")
else:
    print("No es primo")
