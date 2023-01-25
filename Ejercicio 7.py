print("Si es primo se muestra, sino lo factoriza")

numPrimo = int(input("Escribe un numero: "))

for i in range (2,numPrimo):
       booleanPrimo= True
       if numPrimo%i==0:
        booleanPrimo= False
        print("No es primo")
        
        def descomponer (numPrimo) :
            primos = []

            for j in range(2, numPrimo+1):
                while numPrimo % j == 0:
                    primos.append (j)
                    numPrimo = numPrimo/j
            return primos

        print ("Los numeros a descomponer para conseguir ", numPrimo, " son: ", descomponer(numPrimo))
        break
if(booleanPrimo):
    print("Es primo")