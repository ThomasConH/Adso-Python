Canciones = {"Kanye West" : {"Cancion " : "Saint Pablo", "Duracion" : 6.12, "Genero" : "Hip Hop"},
"Julio Jaramillo" : {"Cancion " : "reminiscencias","Duracion" : 3.05, "Genero" : "Bolero"},
"Mac Miller" :{"Cancion 1" : "Self Care", "Duracion" : 5.45, "Genero" : "Hip Hop"} 
}

print("Programa para eliminar un artista")
def EliminarCan(Canciones):
    print("Las Canciones son: ",Canciones)
    Artis = input("Busca el artista que quieras eliminar: ")
    if Artis in Canciones:
        del(Canciones[Artis]) 
        print(Canciones)
    if Artis not in Canciones:
        print("Usted no tiene a este artista en la biblioteca")
EliminarCan(Canciones)