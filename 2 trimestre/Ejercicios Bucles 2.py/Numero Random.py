import random


N = random.randint(1, 100)

Intentos = 0

Jugando = True
print("Adivina el Numero Programa del 1 al 100")

while Jugando:
    Intentos += 1
    E = int(input("Digita un numero: "))
    if E == N:
        print("---Correcto. Fin del programa")
        print("---El numero de intentos que te tomo fueron: ", Intentos,"Intentos")
        Jugando = False
    elif E > N:
        print("--El numero es mas bajo")
        print("-LLevas",Intentos,"Intentos")
    elif E < N:
        print("--El numero es mas alto")
        print("-LLevas",Intentos,"Intentos")
    else:
        print("error")
