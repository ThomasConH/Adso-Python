import random

def divi():
    print("Programa para division")
    Dividendo = random.randint(1,100)
    divisor = int(input(print("Digita el divisor: ")))
    try:
        division = Dividendo / divisor
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    
    print(division)

divi()