#Cual es el valor numerico de acuerdo a los códigos del alfabeto 3


def codabc():
    numeros = {}
    cod = "abcdefghijklmnopqrstuvwxy"
    for i in cod:
        val = ord(i)
        numeros[i]=val
    
    print(numeros)



codabc()