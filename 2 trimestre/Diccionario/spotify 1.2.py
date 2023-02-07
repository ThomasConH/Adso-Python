Canciones = {"Saint Pablo" : { "Artista" : "Kanye West", "Duracion" : 6.12, "Genero" : "Ranchera"}, "reminiscencias" : { "Artista" : "Julio Jaramillo","Duracion" : 3.05,
"Genero" : "Bolero"}, "Self Care" :{"Artista" : "Mac Miller", "Duracion" : 5.45, "Genero" : "Hip Hop" }}

print("Programa para buscar cancion")

def BuscarCanci(Canciones):
    cancion = input("Ingrese el nombre del artista: ")
    for y, x in Canciones.items():
        if cancion == x["Artista"]:
            print("La cancion de este artista es: ",y)

"""def BuscarCanci (Canciones):
    while True:
        cancion = input("Digite el nombre de la cancion: ")
        if cancion == "":
            break
        if cancion in Canciones:
                print(Canciones[cancion])
        if cancion not in Canciones:
                print("La cancion no esta en la playlist")"""


BuscarCanci(Canciones)
