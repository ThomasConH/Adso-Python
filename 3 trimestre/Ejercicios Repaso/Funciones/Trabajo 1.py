import random


def Lista():
    Numeros = []
    Numerospares = []
    numero = int(input(print("Elija una cantidad de numeros pares que quieras añadir a la lista: ")))
    Numeros.append(random.randint(1,10000) in range(numero)) 
    for i in Numeros:
        if Numeros % 2 == 0:
            Numerospares.append(i)
    print(Numerospares)


Lista()
