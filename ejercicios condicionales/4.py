print("cuestionario")

print("Este cuestionario tiene como unica respuesta 'V' (Verdadero) 'F' (Falso)")
print("El programa solo reconocera las respuestas en Mayusculas")

Pregunta1 = "¿Fue Colon la persona que descubrio America?"
Pregunta2 = "¿La independencia de Colombia fue en el año 1810?"
Pregunta3 = "¿The doors era un grupo de Rock Americano?"

Respuesta1 = "V"
Respuesta2 = "V"
Respuesta3 = "V"

Formulacion1 = input(f"Pregunta 1 : {Pregunta1}")
Formulacion2 = input(f"Pregunta 2 : {Pregunta2}")
Formulacion3 = input(f"Pregunta 3 : {Pregunta3}")

aciertos1 = False
aciertos2 = False
aciertos3 = False

#Pregunta 1
if (Formulacion1 == Respuesta1):
    aciertos1 = True

else:
    aciertos1 = False

#Pregunta 2
if (Formulacion2 == Respuesta1):
    aciertos2 = True

else:
    aciertos2 = False

#Pregunta 3
if (Formulacion3 == Respuesta1):
    aciertos3 = True

else:
    aciertos3 = False

#Respuesta 1
if (aciertos1 == True):
    print("Pregunta 1 Es Correcta")

else:
    print("pregunta 1 Es incorrecta")

#Respuesta 2
if (aciertos2 == True):
    print("Pregunta 2 Es Correcta")

else:
    print("pregunta 2 Es incorrecta")
#Respuesta 3
if (aciertos3 == True):
    print("Pregunta 3 Es Correcta")

else:
    print("pregunta 3 Es incorrecta")