#7 8 9 10
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

vector = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
    cont += 1
    suma += vector[i]
    promedio  = suma / cont

    """ Desviación estandar"""
    a = int((vector[i]) - promedio)**2 / cont
    acum = acum + a
    desEstandar = (int(acum)**0.5)

    """Moda"""
    cont2 = 0

    for j in range (r):
        if (vector[i]==vector[j]):
            cont2 = cont2 + 1
    #print('Vector[',i,']= ',vector[i],'se repite',cont2,'veces')

    if cont2 > mayor:
        mayor = cont2
        moda = vector[i]

"""Mediana"""
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
print('La moda de los números generados es:',moda, 'y este se repite',mayor,'veces')
print('La mediana de los números generados es:',mediana)
print('La desviación estandar de los números generados es:',desEstandar)