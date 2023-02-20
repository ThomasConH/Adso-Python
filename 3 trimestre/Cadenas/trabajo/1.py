#Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez 1


def abc():
    abecedario = "asjdlajsfbaskjfnasdflrhgqpjgln"
    letras = []
    tamaño = len(abecedario)
    
    for i in abecedario:
        if i not in letras:
            letras.append(i)
    tamaño2 = len(letras)
    print(abecedario)
    print(letras)
    print("el abecedario tiene",tamaño,"letras")
    print("El abecedario sin repetir tiene",tamaño2,"letras")

abc()   