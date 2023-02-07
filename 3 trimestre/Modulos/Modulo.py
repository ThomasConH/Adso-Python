#Programas de modulo para exportar 
import random


"""def listaS ():
    lis = []
    Numeros = random.randrange(1,100,random.randint(1,10))
    rango = int(input("Digite cuantos numeros quiere que se sumen: "))
    for Numeros in range (rango):
        lis.append(Numeros)
    print(lis)
    print("La suma de los numeros es:",(sum(lis)))

listaS()"""


"""def Diccionarios ():
    Diccionario = {"Pedro Navaja" : "Ruben Blades", "Juanito Alimaña" : "Hector Lavoe", "Me tienes loco" : "Ismael Rivera"}
    print(Diccionario)
    print("1 = Si \n 2 = No")
    resposta = int(input(print("Desea añadir cancion? ")))
    if resposta == 1:
            Cancion = input(print("Digite el nombre de la cancion"))
            Artista = input(print("Digite el nombre del artista"))
            Diccionario[Cancion] = Artista
            print(Diccionario)
    else:
        print("Fin de la funcion")

Diccionarios()"""

"""def Diccionario2 ():
    Diccionario = {"Pedro Navaja" : "Ruben Blades", "Juanito Alimaña" : "Hector Lavoe", "Me tienes loco" : "Ismael Rivera"}
    print(Diccionario)
    print("1 = Si \n 2 = No")
    resposta = int(input(print("Desea eliminar cancion? "))) 
    if resposta == 1:
        cancionel = input(print("Diga el nombre de la cancion a eliminar"))
        del(Diccionario[cancionel])
        print(Diccionario)

Diccionario2()"""



"""def solucion ():
    
    
    A = int(input("Digite el primer Numero: "))
    B = int(input("Digite el segundo Numero: "))
    C = int(input("Digite el tercer Numero: "))
    
    
    if A == B == C:
        print("Los tres numeros se repiten")#check
    elif A == C:
        print("El primer numero y el tercer numero son iguales")#check
    elif B == C:
        print("el segundo numero y el tercer numero son iguales")#Check
    elif A == B:
        print("el primer numero y el segundo numero son iguales")#Check
    else:
        print("ningun numero se repite")#Check

solucion()"""


rango = random.randint(10,25)
vector = []
cont = 0
var = 0
cant = 0
cantidad = 0
var2 = 0
def Pares (rango, vector, cont, var, cant, cantidad, var2):
    for i in range(rango):
        vector.append(round(random.random()*100))
    print(vector)
    print(vector.__len__())
    for i in range(rango):
        if vector[i] %2 == 0:
            cont += 1
            var += vector[i]
        else:
            cant += 1
            var2 += vector[i]
    print("la cantidad total de pares fue: ",cont)
    print("la suma de los numeros pares es: ",var)

Pares(rango, vector, cont, var, cant, cantidad, var2)