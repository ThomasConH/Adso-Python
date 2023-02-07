#Buscar los divisores de un número ingresado por teclado.

def divisores():
    numero = int(input(print("Digite el numero a revisar: ")))
    for i in range(1, numero + 1):
        if numero % i == 0:
            print("Los divisores de", numero, "son: ", i)


divisores()