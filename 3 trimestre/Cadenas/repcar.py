#cuantas veces se repite un caracter dado 4

def rep():
    cod = input("Digite los valores: ")
    letras = []
    tamaño = len(cod)
    contador = 0

    for i in cod:
        if i not in letras:
            letras.append(i)
        elif i in letras:
            contador = contador + 1
    tamaño2 = len(letras)
    print(letras)
    print("el abecedario tiene",tamaño,"letras")
    print("El abecedario sin repetir tiene",tamaño2,"letras")
    print("Los caracteres se repiten",contador,"Veces")

rep() 