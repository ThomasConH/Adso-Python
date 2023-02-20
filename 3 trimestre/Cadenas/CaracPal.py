#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.

def CaraPal():
    Vocalestil = ["á","é","í","ó","ú"]
    vocales = ["a","e","i","o","u"]
    Consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    EspecCar = [".", ",", "ñ", "*", "+", "-", "/", "'"]
    cont = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    Pala = input("Digite la palabra que va a detectar: ")
    for i in vocales:
        if i in Pala:
            cont = cont + 1
    for x in Vocalestil:
        if x in Pala:
            cont1 = cont1 + 1
    for j in Consonantes:
        if j in Pala:
            cont2 = cont2 + 1
    for e in EspecCar:
        if e in Pala:
            cont3 = cont3 + 1
    print("La palabra que digito es:",Pala)
    print("La palabra contiene",cont,"Vocales")
    print("La palabra contiene",cont1,"Vocales con tilde")
    print("La palabra contiene",cont2,"Consonantes")
    print("La palabra contiene",cont3,"Caracteres especiales")

CaraPal()
