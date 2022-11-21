
print("Programa de identificacion de notas")

A = int(input("Ingrese la nota del estudiante: "))

#Solucion
if A<=5:
    print("Reprobado")

elif A == 6:
    print("Aprobado")

elif A == 7:
    print("Suficiente")

elif A == 8:
    print("Bien")

elif A == 9:
    print("Muy Bien")

elif A == 10:
    print("Excelente")

elif A > 10:
    print("Nota no registrada")