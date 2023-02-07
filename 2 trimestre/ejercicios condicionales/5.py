print("Programa que detecta el mes del año en correspodencia del dia")

D = int(input("Digite el dia del año del dia 1 al 365: "))

if D <= 31:
    print("Enero")

elif D <= 59:
    print("Febrero")

elif D <= 90:
    print("Marzo")

elif D <= 120:
    print("Abril")

elif D <= 151:
    print("Mayo")

elif D <= 181:
    print("Junio")

elif D <= 212:
    print("Julio")

elif D <= 243:
    print("Agosto")

elif D <= 273:
    print("Septiembre")

elif D <= 304:
    print("Octubre")

elif D <= 334:
    print("Noviembre")

elif D <= 365:
    print("Diciembre")

else:
    print("error, el numero es mas de 365")