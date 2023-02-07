Canciones = {"Kanye West" : {"Cancion " : "Saint Pablo", "Duracion" : 6.12, "Genero" : "Hip Hop"},
"Julio Jaramillo" : {"Cancion " : "reminiscencias","Duracion" : 3.05, "Genero" : "Bolero"},
"Mac Miller" :{"Cancion 1" : "Self Care", "Duracion" : 5.45, "Genero" : "Hip Hop"} 
}

print("Programa para bibliografia de un artista")
def BuscarArt(Canciones):
    while True:
        Nombre = input("Busca el artista: ")
        if Nombre == "":
            print("Fin de la funcion")
            break
        if Nombre in Canciones:
            print(Canciones[Nombre])
        if Nombre not in Canciones:
            print("Usted no tiene a este artista en la biblioteca")
BuscarArt(Canciones)



