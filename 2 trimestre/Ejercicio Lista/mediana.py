import random

cont = 0
mediana = 0

vector = []
ordenados = []
r = len(vector)

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
    cont += 1

    for j in range (r):
        if vector[i]>vector[j]:
            vector[i]=vector[j]


if rango % 2 > 0:
    mediana = vector[rango//2]
else:
    n1 = vector[rango//2]
    n2 = vector[rango//2 - 1]
    mediana = (n1 + n2) / 2

print('Se generaron',rango,'numeros aleatorios que son',vector)
print(ordenados)