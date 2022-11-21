#4
import random

vector = []
n = int(0)
numeros = random.randint(10,25)
for i in range(numeros):
    vector.append(round(random.random()*100))
print("Lista: ",vector)
print("La cantidad de numeros en la lista: ",vector.__len__())

a = False
b = False
while a == False:
    a == True
    for i in range (len(vector)-1):
        if vector[i] > vector[i+1]:
            h = vector[i]
            vector[i] = vector[i+1]
            vector[i+1] = h
            a = False

print("El orden de la lista de mayor a menor: ",vector)

while b == False:
    b = True
    for n in range(len(vector)-1):
        if vector[n] < vector[n+1]:
            p = vector[n]
            vector[n] = vector[n+1]
            vector[n+1] = p
            b = False

print("El orden de la lista de menor a mayor: ",vector)