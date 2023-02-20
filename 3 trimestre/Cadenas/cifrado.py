#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin. 9

def cifrado():
    texto=input('Escriba la palabra a buscar: ').lower()
    codigo=['m','u','r','c','i','e','l','a','g','o']
    print("murcielago")
    print("0123456789")
    salida=''
    for i in range(len(texto)):
        if texto[i] in codigo:
            salida+=str(codigo.index(texto[i]))
        else:
            salida+=texto[i]
    print(salida)
cifrado()