import random




T = int(input("Digite el tamaño de la lista de numeros, desde el 10 hasta el 25: "))
V = []
S = 0
P = 0
M = 0


if T < 10:
    print("Solo se haran las operaciones si la cantidad de numeros es mas de 10 y menos que 25")

elif T > 25:
    print("Solo se haran las operaciones si la cantidad de numeros es mas de 10 y menos que 25")


else:
    for I in range(T):
        V.append(round(random.randint(10, 25)))
#Suma
    for I in V:
        S = S + I
#Promedio
    for X in V:
        P = S / T
#Moda
    M = len(V)
    N = 0
    mayor = 0
    for K in range(M):
        N = 0
        for J in range (M):
            if V[K] == V[J]:
                N = N + 1
        if N > mayor:
            mayor = N
            moda = V[K]
#Mediana
    print("La lista es: ",V)
    V.sort()
    if M %2 > 0:
        mediana = V[M//2]
    else:
        num1 = V[M//2]
        num2 = V[M//2-1]
        mediana = (num1 + num2)/2


    print("Los numeros ordenados son: ",V)
    print("La suma de los numeros es: ",S)
    print("el promedio de los numeros es: ",P)
    print("la moda de los numeros es ",moda)
    print("la mediana de los numeros es: ",mediana)
    
