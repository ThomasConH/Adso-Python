#Introduccion de valores

a = int(input("Digite el primer numero: "))
b = int(input("Digite el primer numero: "))
c = int(input("Digite el tercer numero: "))

#Solucion

Nmenor = min(a, b, c)
Nmayor = max(a, b, c)
valor_medio = (a+b+c) - Nmenor - Nmayor

print(Nmenor, valor_medio, Nmayor)

print("el numero medio es", valor_medio)