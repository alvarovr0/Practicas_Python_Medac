def mayor(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        print("El mayor es: ", n1)
    elif n2>=n1 and n2>=n3:
        print("El mayor es: ", n2)
    elif n3>=n1 and n3>=n2:
        print("El mayor es: ", n3)

def mayor1(n1,n2,n3):
    mayor=0
    if n1>=n2 and n1>=n3:
        mayor=n1
    elif n2>=n1 and n2>=n3:
        mayor=n2
    elif n3>=n1 and n3>=n2:
        mayor=n3
    return mayor
mayor(3,4,1)

print("El mayor es: ", mayor1(12,54,153))
