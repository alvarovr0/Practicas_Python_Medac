print("Primos anteriores")

numPrimo = int(input("Escribe un numero: "))

for i in range(2, numPrimo):
    primo= True
    for j in range(2,i):
        if i%j ==0:
            primo=False
            break
    if primo:
        print(i)
