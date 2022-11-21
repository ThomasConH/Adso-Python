r = int(input("Digite un numero de maximo 2 cifras: "))
n = int(input('Digite un numero de maximo 2 cifras: '))


Inicio = False
def MayoMen (r, n):
    Inicio = True
    while Inicio == True :
        if r > n:
            print("El primer numero que digito es mayor que el segundo")
            Inicio = False
        elif r < n:
            print("El segundo numero que digito es mayor que el primero")
            Inicio = False
        elif r == n:
            print("Usted digito el mismo numero")
            Inicio = False
        elif (r or n) > 100:
            print("Error, Solo admitiremos numeros menores de 9 cifras")

MayoMen(r, n)