class Animales:
    def __init__(self,nombre):
        self.nombre = nombre
        self.velocidad = 0

    def cami(self):
        self.velocidad = 5


class Perro(Animales):
    def __init__(self, nombre, ambiente):
        Animales.__init__(self,nombre)
        self.ambiente = ambiente

    def ladrido(self):
        print("guau guau")


Mi_Perro = Perro("Simon","Domestico")
Mi_Perro.cami
print(Mi_Perro.nombre)
print(Mi_Perro.ambiente)