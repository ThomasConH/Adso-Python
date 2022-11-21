def es_numero_perfecto(numero):
    suma = 0
    
    for i in range(1, numero):
        if numero % i ==0:
            suma += i
            
    return suma == numero 


print(es_numero_perfecto())
print(es_numero_perfecto())  
