#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin. 9

def secret():
    texto=input('Digite la palabra que va a cifrar: ').lower()
    codigo="suponiera"
    codigo = list(codigo)
    salida=''
    for i in range(len(texto)):
        if texto[i] in codigo:
            salida+=str(codigo.index(texto[i]))
        else:
            salida+=texto[i]
    print(salida)
secret()