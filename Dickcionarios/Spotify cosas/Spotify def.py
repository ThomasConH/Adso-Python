Canciones = {"Saint Pablo" : { "Artista" : "Kanye West", "Duracion" : 6.12, "Genero" : "Ranchera"},
"reminiscencias" : { "Artista" : "Julio Jaramillo","Duracion" : 3.05,"Genero" : "Bolero"},
"Self Care" :{"Artista" : "Mac Miller", "Duracion" : 5.45, "Genero" : "Hip Hop" }, 
"Miracle Man" : {"Artista" : "Oliver Tree", "Duracion" : 2.05, "Genero" : "Pop"},
"Die For You" : {"Artista" : "Joji", "Duracion" : 3.31, "Genero" : "Sad Balad"}}

#Funciones:
def BuscarArt(Canciones):
    print("Programa para buscar artista de cancion")
    while True:
        nombre = input("Ingrese el nombre del artista: ")
        for y, x in Canciones.items():
            if nombre == x["Artista"]:
                print("La cancion de este artista es: ",y)
        if nombre == "":
            print("Fin de la funcion")
            break

def BuscarCanci (Canciones):
    print("Programa para buscar cancion de artista")
    while True:
        cancion = input("Digite el nombre de la cancion: ")
        if cancion == "":
            print("Fin de la Funcion")
            break
        if cancion in Canciones:
                print(Canciones[cancion])
        if cancion not in Canciones:
                print("La cancion no esta en la playlist")

def EliminarCan(Canciones):
    print("Programa para eliminar una cancion")
    print("")
    print("Esta es tu playlist ",Canciones)
    print("")
    while True:
        cancion = input("Busca la cancion que quieras eliminar ")
        if cancion == "":
            print(Canciones)
            break
        if cancion in Canciones:
            del(Canciones[cancion]) 
            print(Canciones)
        if cancion not in Canciones:
            print("Usted no tiene a este artista en la biblioteca")

def DuracionMas(Canciones):
    Dur = []
    for y,x in Canciones.items():
        Duracion = x["Duracion"],y
        Dur.append(Duracion)
        Dur.sort()
    print("La cancion que mas duracion tiene es: ",Dur[-1])

def DuracionMenos(Canciones):
    Dur = []
    for y,x in Canciones.items():
        Duracion = x["Duracion"],y
        Dur.append(Duracion)
        Dur.sort()
    print("La cancion que menos duracion tiene es: ",Dur[0])



print("La playlist suya es:",Canciones)
print("")
print("1 = Buscar Artistas")
print("2 = Buscar Canciones")
print("3 = Eliminar Cancion")
print("4 = Verificar cual cancion tiene mas duracion")
print("5 = verificar cual cancion tiene menos duracion")
print("")
Answer = int(input("Digite la funcion que quiere que se ejecute: "))
if Answer == 1:
    BuscarArt(Canciones)
elif Answer == 2:
    BuscarCanci(Canciones)
elif Answer == 3:
    EliminarCan(Canciones)
elif Answer == 4:
    DuracionMas(Canciones)
elif Answer == 5:
    DuracionMenos(Canciones)
else:
    print("Error")