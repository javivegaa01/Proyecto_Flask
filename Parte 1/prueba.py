continuar=input("¿Quieres empezar a ver las ligas de los paises? (s/n)")
lista=['a','b','c']
while continuar=="s":
    for a in lista:
        print(a)
        continuar=input("¿Quieres ver otro? (s/n)")
        if continuar=="n":
            break