#Este ejercicio es mio


Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def nose(Lista):
    for i in Lista:
        if i % 2 == 0:
            print("numero par:", i)
        elif i % 2 != 0:
            print("Numero impar:", i)


nose(Lista)

