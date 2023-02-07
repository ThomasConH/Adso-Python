"""Canciones = {"Kanye West" : {"Cancion " : "Saint Pablo", "Duracion" : 6.12, "Genero" : "Hip Hop"},
"Julio Jaramillo" : {"Cancion " : "reminiscencias","Duracion" : 3.05, "Genero" : "Bolero"},
"Mac Miller" :{"Cancion 1" : "Self Care", "Duracion" : 5.45, "Genero" : "Hip Hop"} 
}"""

Canciones = {"Saint Pablo" : { "Artista" : "Kanye West", "Duracion" : 6.12, "Genero" : "Ranchera"},
"reminiscencias" : { "Artista" : "Julio Jaramillo","Duracion" : 3.05,"Genero" : "Bolero"},
"Self Care" :{"Artista" : "Mac Miller", "Duracion" : 5.45, "Genero" : "Hip Hop" }}

print("Programa para eliminar un artista")
def EliminarCan(Canciones):
    print("Programa para eliminar una cancion")
    print("")
    print("Esta es tu playlist ",Canciones)
    print("")
    while True:
        cancion = input("Escribe la cancion que quieras eliminar: ")
        if cancion == "":
            print(Canciones)
            print("Fin de la Funcion")
            break
        if cancion in Canciones:
            del(Canciones[cancion]) 
            print(Canciones)
        if cancion not in Canciones:
            print("Usted no tiene a este artista en la biblioteca")
EliminarCan(Canciones)