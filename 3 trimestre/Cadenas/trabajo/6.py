#Determinar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula 6
#"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"


def Pal():
    Vocales = ["á", "é", "í", "ó", "ú"]
    letrasag = ["n", "s"]
    texto = input("Digite la palabra: ")
    texto.lower()
    for i in Vocales:
        for x in letrasag:
            if i in texto[-1] and x in texto[-1]:
                print("Es aguda")
                break
            if i in texto[-2]:
                print("Es grave")
                break
            if i in texto[-3]:
                print("es esdrujula")
            if i in texto[-4]:
                print("Es sobreesdrujula")
Pal()

#range(len[texto])