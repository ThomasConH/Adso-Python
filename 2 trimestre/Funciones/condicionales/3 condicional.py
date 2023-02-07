horas = int(input("Digite el numero de horas de trabajo: "))
    
    
def calculo():
    if horas >= 41:
        extras = horas - 40
        salarioex = (horas * 2600) + (extras * 5000)
        return "El salario por",horas," es de: ",salarioex
    else:
        salarionormal = horas * 2600
        return "El salario por",horas," horas es de: ",salarionormal

print(calculo())