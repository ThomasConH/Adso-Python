#Planteamiento

from ast import If


print("Programa que determina la igualdad y desigualdad de tres numeros")

A = int(input("Digite el primer Numero: "))
B = int(input("Digite el segundo Numero: "))
C = int(input("Digite el tercer Numero: "))

#Solucion

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