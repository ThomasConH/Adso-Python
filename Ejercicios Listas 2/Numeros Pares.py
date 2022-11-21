import random

rango = random.randint(10,25)
vector = []

for i in range(rango):
    vector.append(round(random.random()*100))
print(vector)
print(vector.__len__())
cont = 0
var = 0
cant = 0
cantidad = 0
var2 = 0

for i in range(rango):
    if vector[i] %2 == 0:
        cont += 1
        var += vector[i]
    else:
        cant += 1
        var2 += vector[i]

print("la cantidad total de pares fue: ",cont)
print("la suma de los numeros pares es: ",var)