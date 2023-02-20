#Pida una cadena por teclado y diga cual es su valor al sumar sus codigos 2 

def cod():
    numeros = []
    sum = 0
    cod = input("Digite el codigo de letras a sumar: ")
    for i in cod:
        val = ord(i)
        numeros.append(val)
    for x in numeros:
        sum += x
    
    print(numeros)
    print(sum)


cod()