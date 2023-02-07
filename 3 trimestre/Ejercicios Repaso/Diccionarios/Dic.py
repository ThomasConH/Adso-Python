#Preguntar al usuario por un animal que se va a agregar al diccionario con su respectivo valor que es la traducción en inglés que también se le va a preguntar al usuario.


Diccionario = {"Gato" : "Cat", "Perro" : "Dog", "Goat" : "Cabra"}

def Dick (Diccionario):
    print("Añadir palabras en español y en ingles")
    palabraesp = input(print("Digite la palabra en español"))
    palabraing = input(print("Digite el significado en ingles"))
    Diccionario[palabraesp] = palabraing

    print(Diccionario)

Dick(Diccionario)