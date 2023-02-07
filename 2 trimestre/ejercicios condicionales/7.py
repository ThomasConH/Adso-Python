print("Programa de calculo de costo de llamadas")

C = int(input("Digite el tiempo en minutos que ha estado en la llamada: "))

if C <= 3:
    print("El precio por ",C,"minutos es de 200 pesos")

elif C > 3:
    C1 = C - 3
    C2 = C1 / C1
    C3 = C2 = 50 
    C4 = C3 * C1
    C5 = C4 + 200
    print("El precio por ",C,"Minutos de llamada es de: ",C5) 