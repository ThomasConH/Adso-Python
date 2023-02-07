print("Sistema de Calculo de Salario: ")

S = int(input("Ingrese el numero de horas que trabajo"))

if S > 40:
    SE = S - 40
    SA = (40 * 2.600) + (SE * 5000)
    print("El salario ganado por ",S,"Horas de trabajo es: ", SA)

elif  S <= 40:
    SM = S/40*2600*40
    print("El salario luego de ",S,"Horas de trabajo es de: ",SM)

print("Fin de la operacion")