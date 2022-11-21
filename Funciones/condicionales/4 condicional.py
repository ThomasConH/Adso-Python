minutos = int(input("Digite el numero de minutos que estuvo en llamada: "))

def calculo():
    if minutos <= 3:
        return "el precio por",minutos," es de: 200 pesos"
    else:
        c1 = minutos - 3
        c2 = c1 / c1
        c3 = c2 = 50
        c4 = c3 * c1
        c5 = c4 + 200
        return "el precio por ",minutos," es de: ",c5,"pesos"

print(calculo())