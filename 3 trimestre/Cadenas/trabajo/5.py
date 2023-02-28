#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas 5

def may():
    cod = input("Digite la cadena: ")
    print("La cadena en mayuscula es:",cod.upper())
    print("La cadena en minuscula es:",cod.lower())
    print("La cadena donde se diversifican las mayusculas y minusculas:",cod.swapcase())
    print("La cadena donde las primeras letras despues del espacio se convierten en mayusculas:",cod.title())

may()