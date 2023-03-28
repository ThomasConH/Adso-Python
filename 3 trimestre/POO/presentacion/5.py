#Herencia Multiple
#Es cuando una clase, es heredada por otras dos o mas clases con el fin de definir los datos de esa clase

class Estudiante:
    def __init__(self,nombre,ficha):
        self.nombre = nombre
        self.ficha = ficha

class City(object):
    domicilio = "Soacha"

class Presentacion(Estudiante,City):
    def yo(self):
        print("Hola mi nombre es",self.nombre,"Vivo mi ficha es la numero",self.ficha)
        print("Estudio en el cide")
        print("Vivo en",self.domicilio)


personaje = Presentacion("Jesse","2560664")
personaje.yo()
