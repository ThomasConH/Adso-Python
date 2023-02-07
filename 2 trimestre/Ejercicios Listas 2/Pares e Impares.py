#3
import random

rango = random.randint(10,25)
vector = []

for i in range(rango):
    vector.append(round(random.random()*100))
print(vector)
print("La cantidad de numeros en la lista es de: ",vector.__len__())
cont = 0
var = 0
cant = 0
cantidad = 0
var2 = 0

for i in range(rango):
    if vector[i] %2 == 0:
        cont += 1
        var += vector[i]
        pares = var // cont
    else:
        cant += 1
        var2 += vector[i]
        impares = var2 //cant

print("la suma de los numeros pares es: ",var)
print("El promedio de numeros pares es de: ",pares)
print("La suma de los numeros impares es: ",var2)
print("el promedio de impares es: ",impares)