nota = int(input("Ingrese la nota del estudiante: "))

def Puntaje():
    if nota <=5:
        return "Reprobado"
    elif nota == 6:
        return "Aprobado"
    elif nota == 7:
        return "Suficiente"
    elif nota == 8:
        return "Bien"
    elif nota == 9:
        return "Muy bien"
    elif nota == 10:
        return "Excelente"
    else:
        return "Nota no registrada"


print(Puntaje())