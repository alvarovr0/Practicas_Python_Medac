x = 0
x1 = 1
x2 = 1
print(x1)
print(x2)

for i in range(50):
    x=x1+x2
    x1=x2
    x2=x
    print(x)
    print("Número aureo", x2/x1)
