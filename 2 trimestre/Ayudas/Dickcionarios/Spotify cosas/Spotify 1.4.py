Canciones = {"Saint Pablo" : { "Artista" : "Kanye West", "Duracion" : 6.12, "Genero" : "Ranchera"},
"reminiscencias" : { "Artista" : "Julio Jaramillo","Duracion" : 3.05,"Genero" : "Bolero"},
"Self Care" :{"Artista" : "Mac Miller", "Duracion" : 5.45, "Genero" : "Hip Hop" }}


Dur = []

for y,x in Canciones.items():
    Duracion = y,x["Duracion"]
    Dur.append(Duracion)
    Dur.sort()
print(Dur[0])