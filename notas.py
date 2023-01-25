print("Notas")
nota1=int(input("Escribe la primera nota "))
nota2=int(input("Escribe la segunda nota "))
nota3=int(input("Escribe la tercera nota "))

suma=nota1+nota2+nota3

media=suma/3

if media<5:
    print("Suspenso")
if media>=5 and media<7:
    print("Aprobado")
if media>=7 and media<9:
    print("Notable")
if media>=9 and media<10:
    print("Sobresaliente")
elif media>10:
    print("Nota fuera de rango")
