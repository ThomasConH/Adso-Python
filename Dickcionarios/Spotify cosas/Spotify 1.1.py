Canciones = {"Rocio Durcal" : { "Cancion" : "La gata bajo la lluvia", "Duracion" : 3.27, "Genero" : "Ranchera"}, "Julio Jaramillo" : { "Cancion" : "reminiscencias","Duracion" : 3.05,
"Genero" : "Bolero"}, "Mac Miller" :{"Cancion" : "Self Care", "Duracion" : 5.45, "Genero" : "Hip Hop" }}

print("Programa para bibliografia de un artista")
def BuscarArt(Canciones):
    Nombre = input("Busca el artista: ")
    if Nombre in Canciones:
        print(Canciones[Nombre])
    if Nombre not in Canciones:
        print("Usted no tiene a este artista en la biblioteca")
BuscarArt(Canciones)



