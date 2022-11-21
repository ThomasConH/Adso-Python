Canciones = {"La gata bajo la lluvia" : { "Artista" : "Rocio Durcal", "Duracion" : 3.27, "Genero" : "Ranchera"}, "reminiscencias" : { "Artista" : "Julio Jaramillo","Duracion" : 3.05,
"Genero" : "Bolero"}, "Self Care" :{"Artista" : "Mac Miller", "Duracion" : 5.45, "Genero" : "Hip Hop" }}

print("Programa para buscar cancion")
def BuscarCanci (Canciones):
    cancion = input("Digite el nombre de la cancion: ")
    if cancion in Canciones:
        print(Canciones[cancion])
    if cancion not in Canciones:
        print("La cancion no esta en la playlist")


BuscarCanci(Canciones)
