#realice un programa el  cual  determine cual es la  potencia de un ciclista en un cierto tiempo determinado
print("Programa para calcular la potencia de un ciclista en determinado tiempo")
print("Potencia = Masa * Velocidad^2 / 2")
M = int(input("Digite el peso del ciclista: "))
V = int(input("Digite la velocidad del ciclista en Km/h:"))
Ek = M * V**2 /2
print("La potencia del ciclista es: ",Ek,"Jules") 