#1
import random

rango = random.randint(10,25)
vector = []
veccant = []

for i in range(rango):
    vector.append(round(random.random()*100))
print(vector)
cont = 0
var = 0
cantidad = 0
var2 = 0

for i in range(rango):
    cont += 1
    var += vector[i]
    promedio =  var // cont
print("la suma de los numeros es: ",var)
print("el promedio es: ",promedio)
for k in vector:
    if k < promedio:
        print(k," Es menor que el promedio")
    elif k > promedio:
        print(k, " Es mayor al promedio")
    else:
        print(k," Es el promedio")