import random
#Numeros aleatorios que uno quiera
'''T = int(input("Digite Cuantos numeros: "))
V = []
for I in range(T):
    V.append(round(random.random()*100))

print(V)'''

#Mostrar posiciones y numeros
'''T = int(input("Digite Cuantos numeros: "))
V = []
for I in range(T):
    V.append(round(random.random()*100))
    print(V.__len__())

for I in range(T):
    print("Posicion ",I," Elemento",V[I])

print(V)'''

#Pares o impares

'''T = int(input("Digite Cuantos numeros: "))
V = []
for I in range(T):
    V.append(round(random.random()*100))

Cont = 0
Cont2 = 0

for I in range(T):
    if V [I]%2==0:
        print(V[I], "Es par")
        Cont += 1
        
    else:
        print(V[I], "Es impar")
        Cont2 += 1
        
print("Hay",Cont," numeros pares")
print("Hay",Cont2," Numeros impares")'''

#suma de pares e impares

T = int(input("Digite Cuantos numeros: "))
V = []
for I in range(T):
    V.append(round(random.random()*100))

Cont = 0
Cont2 = 0

for I in range(T):
    if V [I]%2==0:
        print(V[I], "Es par")
        Cont += 1
        
    else:
        print(V[I], "Es impar")
        Cont2 += 1
        
print("Hay",Cont," numeros pares")
print("Hay",Cont2," Numeros impares")
