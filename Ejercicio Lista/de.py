cont = 0
suma = 0
acum = 0

vector = [9,3,8,8,9,8,9,18]
r = len(vector)

for i in range(r):
    cont += 1
    suma += vector[i]
    promedio  = suma / cont

    # Desviación estandar
    a = int((vector[i]) - promedio)**2 / cont
    acum = acum + a
    rc = (int(acum)**0.5)

print(int(acum))
print(rc)



