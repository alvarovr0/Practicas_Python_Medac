print("Escribe los lados de un triangulo")

lado1=int(input("Introduce el primer lado: "))
lado2=int(input("Introduce el segundo lado: "))
lado3=int(input("Introduce el tercer lado: "))

if lado1==lado2 and lado2==lado3:
    print("El triángulo es equilatero")
if (lado1!=lado2 and lado2==lado3) or (lado1==lado2 and lado2!=lado3) or (lado1==lado3 and lado2!=lado1):
    print("El triángulo es isósceles")
if lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
    print("El triángulo es escaleno")
