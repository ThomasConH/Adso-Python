import random

Vector = []

Rango = random.randint(1,25)

for i in range(Rango):
    Vector.append(round(random.random()*100))


print(Vector)