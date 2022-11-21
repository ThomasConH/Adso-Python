N = int(input("Digitar numero de tres cifras: "))

def SumaCubos(N):
    if N > 999:
        print("Solo numeros de mas de tres cifras")
    elif N < 100:
        print("Solo numeros de tres cifras")
    else:
            U=N %10
            N=N //10
            D=N%10
            N=N//10
            C=N%10
            C3 = C * C * C
            D3 = D * D * D
            U3 = U * U * U
            S = C3 + D3 + U3
            print("Los numeros que usted ingreso fueron: ",C, D, U)
            print("Al sumarles el cubo a cada uno es: ",C3,D3,U3)
            print("El resultado de la suma de los 3 numeros juntos al cubo es: ",S)


SumaCubos(N)
