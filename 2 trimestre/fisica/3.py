# Realizar programa en el que el usuario ingrese ciertos datos
# Para que una grua permita elevar materiales de construccion

print("Determinar la fuerza de la grua")

M = int(input("Ingrese el peso de los materiales: "))
G = int(input("Ingrese el peso de la canasta: "))
F = M * G

print("Ahora se determina el trabajo de la grua")
D = int(input("Ingrese la altura donde se subiran los materiales: "))
W = F * D

print("Se determinara la potencia")
T = int(input("Ingrese el tiempo previsto en la subida de los materiales: "))
P = W / T

print("La masa de la canasta es: ",M,"Y la potencia del motor es: ",P,"Funciona correctamente")

print("La fuerza de la grua es de: ",F)
print("El trabajo que hace la grua es: ",W)
print("La potencia del trabajo que hizo la grua es: ",P)
