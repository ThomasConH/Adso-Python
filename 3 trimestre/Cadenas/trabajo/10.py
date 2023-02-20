#Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última 10

def Subca():
    cod = input("Digite los valores: ")
    letras = []

    for i in cod:
        letras.append(i)
        print(letras)

Subca()