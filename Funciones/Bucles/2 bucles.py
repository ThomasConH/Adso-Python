import random

print("Juego de numeros random ")

N = random.randint(1, 100)

Intentos = 0

Jugando = False

def Juego(N):
    
    while Jugando == False:
        Intentos = 0
        Intentos += 1
        E = int(input("Digita un numero: "))
        if E == N:
            print("---Correcto. Fin del programa")
            print("---El numero de intentos que te tomo fueron: ", Intentos,"Intentos")
            Jugando = True
        elif E > N:
            print("--El numero es mas bajo")
            print("-LLevas",Intentos,"Intentos")
        elif E < N:
            print("--El numero es mas alto")
            print("-LLevas",Intentos,"Intentos")
        else:
            print("error")
            Jugando == True

Juego(N)