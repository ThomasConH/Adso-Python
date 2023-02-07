import random

cont = 0
cont2 = 0
suma = 0
acum = 0
promedio = 0
mayor = 0
moda = 0
mediana = 0
desEstandar = 0
rango = random.randint(10,25)

vector = []
r = len(vector)

def Boss (cont, cont2, suma, acum, promedio, mayor, moda, mediana, desEstandar):
    for i in range(rango):
        vector.append(round(random.random()*100))
        cont += 1
        suma += vector[i]
        promedio  = suma / cont

        """ Desviación estandar"""
        a = int((vector[i]) - promedio)**2 / cont
        acum = acum + a
        desEstandar = (int(acum)**0.5)

        vector.sort()
        if rango % 2 > 0:
            mediana = vector[rango//2]
    else:
        n1 = vector[rango//2]
        n2 = vector[rango//2 - 1]
        mediana = (n1 + n2) / 2
    print('Se generaron',rango,'numeros aleatorios que son:',vector)
    print('La suma de los números generados es:',suma)
    print('El promedio de los números generados es:',promedio)
    print('La mediana de los números generados es:',mediana)
    print('La desviación estandar de los números generados es:',desEstandar)

Boss(cont, cont2, suma, acum, promedio, mayor, moda, mediana, desEstandar)

