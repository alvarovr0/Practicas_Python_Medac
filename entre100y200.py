cantidad=int(input("¿Cuantos numeros quieres introducir? "))
num100=0
num200=0
for x in range(0, cantidad):
    numero=int(input("Introduce un número "))
    if numero>=0 and numero<=100:
        num100=num100+1
    if numero>100 and numero<=200:
        num200=num200+1

print("Hay ", num100, " números entre 0 y 100")
print("Hay ", num200, " números entre 100 y 200")
