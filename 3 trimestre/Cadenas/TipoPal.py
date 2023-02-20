#Determinar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula 6
#"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"


def Pal():
    Vocales = ["á", "é", "í", "ó", "ú"]
    letrasag = ["n", "s"]
    texto = input("Digite la palabra: ")
    texto.lower()
    for i in Vocales:
        for x in letrasag:
            if i in texto[-2:] and x in texto[-1]:
                print("Es aguda")
                break
            if i in texto[-2:] or x in texto[-1]:
                print("Es aguda")
                break
            if x in texto[0:2]:
                print("es grave")
Pal()

#range(len[texto]) 00
