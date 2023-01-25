print("Saber cuantos digitos tiene un número")
num=int(input("Introduce un número "))

if num>=0 and num<10:
    print("Tiene un digito")
if num>=10 and num<100:
    print("Tiene dos digitos")
if num>=100 and num<1000:
    print("Tiene tres digitos")
